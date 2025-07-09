import time
from datetime import datetime, timedelta

CRAWLER_ID = 1

# لیست بازی‌های فرضی با زمان شروع (برای شبیه‌سازی)
FAKE_MATCHES = [
    {"match_id": "A1", "start_time_utc": datetime.utcnow() + timedelta(minutes=1), "A": 2.1, "B": 58, "C": 170},
    {"match_id": "A2", "start_time_utc": datetime.utcnow() + timedelta(hours=13), "A": 1.5, "B": 62, "C": 180},
    {"match_id": "A3", "start_time_utc": datetime.utcnow() + timedelta(hours=30), "A": None, "B": 50, "C": 190},
]

def log(msg):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    print(f"[CRAWLER {CRAWLER_ID}] [{now}] {msg}")

def is_data_complete(match):
    return all([match.get("A"), match.get("B"), match.get("C")])

def send_to_model_x(match):
    log(f"📤 ارسال بازی {match['match_id']} به مدل X (ساعت محلی + داده کامل)")

def main():
    try:
        log("✅ خزنده ۱ شروع به جمع‌آوری اولیه کرد.")
        time.sleep(1)

        for match in FAKE_MATCHES:
            time_to_start = (match["start_time_utc"] - datetime.utcnow()).total_seconds() / 60

            if time_to_start < 0 or time_to_start > 2880:
                log(f"⏭ بازی {match['match_id']} خارج از بازه ۲ روز آینده. رد شد.")
                continue

            if not is_data_complete(match):
                log(f"❌ بازی {match['match_id']} داده ناقص دارد (رد شد).")
                continue

            log(f"🟢 بازی {match['match_id']} تایید شد ({int(time_to_start)} دقیقه مانده).")
            send_to_model_x(match)
            time.sleep(0.5)

        log("🏁 خزنده ۱ وظیفه جمع‌آوری اولیه را کامل کرد.")

    except Exception as e:
        log(f"❌ خطا در اجرای خزنده: {e}")
        exit(1)

if __name__ == "__main__":
    main()
