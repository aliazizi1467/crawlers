import time
from datetime import datetime, timedelta
import traceback
import requests  # ✅ افزودن این برای ارسال به مدل X

CRAWLER_ID = 3

FAKE_MATCHES = [
    {"match_id": "B1", "start_time_utc": datetime.utcnow() + timedelta(minutes=13), "A": 1.9, "B": 65, "C": 175},
    {"match_id": "B2", "start_time_utc": datetime.utcnow() + timedelta(minutes=25), "A": 2.3, "B": 50, "C": 180},
    {"match_id": "B3", "start_time_utc": datetime.utcnow() - timedelta(minutes=5), "A": 1.7, "B": 60, "C": 160},
]

def log(msg):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    print(f"[CRAWLER {CRAWLER_ID}] [{now}] {msg}")

def is_data_complete(match):
    return all([match.get("A"), match.get("B"), match.get("C")])

def send_to_model_x(match):
    log(f"📤 ارسال بازی {match['match_id']} به مدل X برای مرحله ۳")

    try:
        data = {
            "crawler_id": CRAWLER_ID,
            "match_id": match["match_id"],
            "team": "home",  # اگر تیم میزبان مهم است، این قسمت قابل تغییر است
            "A": match["A"],
            "B": match["B"],
            "C": match["C"],
            "local_time": match["start_time_utc"].strftime("%H:%M"),
            "result": None
        }

        response = requests.post(
            "https://milad-x-api--aliazizi1467.repl.co/receive",  # ✅ آدرس واقعی Replit تو
            json=data
        )

        if response.status_code == 200:
            log(f"✅ ارسال موفق: {response.json()}")
        else:
            log(f"❌ ارسال ناموفق ({response.status_code}): {response.text}")

    except Exception as e:
        log(f"❌ خطای ارتباط با مدل X: {e}")

def main():
    try:
        time.sleep(2)
        log("🚀 خزنده ۳ اجرای واقعی را آغاز کرد.")

        for match in FAKE_MATCHES:
            minutes_to_start = (match["start_time_utc"] - datetime.utcnow()).total_seconds() / 60

            if minutes_to_start < 0:
                log(f"⏱ بازی {match['match_id']} شروع شده (رد شد).")
                continue

            if minutes_to_start > 20:
                log(f"⏭ بازی {match['match_id']} خارج از بازه ({int(minutes_to_start)} دقیقه مانده).")
                continue

            if not is_data_complete(match):
                log(f"❌ داده‌های ناقص برای بازی {match['match_id']} — رد شد.")
                continue

            log(f"🟢 بازی {match['match_id']} واجد شرایط. (مانده: {int(minutes_to_start)} دقیقه)")
            send_to_model_x(match)
            time.sleep(0.5)

        log("✅ خزنده ۳ با موفقیت وظیفه را کامل کرد.")
    
    except Exception as e:
        log("❌ خطای غیرمنتظره در خزنده:")
        traceback.print_exc()
        exit(1)

if __name__ == "__main__":
    main()
