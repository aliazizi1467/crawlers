import time
from datetime import datetime

CRAWLER_ID = 3  # شناسه این خزنده

def log(message):
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    print(f"[Crawler ID: {CRAWLER_ID}] [{now}] {message}")

def main():
    try:
        log("✅ خزنده ۳ شروع شد.")
        time.sleep(1)

        # شبیه‌سازی وظیفه مرحله ۱
        log("🔍 در حال جمع‌آوری بازی‌های ۲ روز آینده...")
        time.sleep(1)

        # شبیه‌سازی بررسی داده A, B, C
        log("📊 بررسی داده‌ها: A, B, C کامل هستند.")
        time.sleep(1)

        # شبیه‌سازی ارسال به مدل X
        log("📤 داده‌ها به مدل X ارسال شدند.")
        time.sleep(1)

        log("✅ خزنده ۳ با موفقیت پایان یافت.")
    
    except Exception as e:
        log(f"❌ خطا در اجرای خزنده: {e}")
        exit(1)

if __name__ == "__main__":
    main()
