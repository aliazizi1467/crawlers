import time
from datetime import datetime

def log(msg):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    print(f"[Crawler ID: 3] [{now}] {msg}")

def main():
    log("✅ خزنده شماره ۳ شروع به کار کرد.")
    time.sleep(2)
    log("📊 وظیفه اولیه خزنده ۳ با موفقیت انجام شد.")
    time.sleep(1)
    log("✅ خزنده شماره ۳ با موفقیت پایان یافت.")

if __name__ == "__main__":
    main()
