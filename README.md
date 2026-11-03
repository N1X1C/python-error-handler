# 🛡️ Python Resilient Exception & Error Handling Architecture

A clean, interactive Python utility demonstrating defensive programming and structured exception handling using `try`, `except`, `finally`, and runtime type verification (`isinstance`).

---

## 🇮🇷 مستندات کامل فارسی (Persian Documentation)

### ۱. معرفی و هدف پروژه
در توسعه نرم‌افزارهای حرفه‌ای، جلوگیری از توقف ناگهانی برنامه (Crash) در مواجهه با ورودی‌های غیرمجاز کاربر اهمیت بالایی دارد. این پروژه یک معماری دفاعی استاندارد در پایتون را برای مدیریت همزمان خطاهای محاسباتی و خطاهای نوع داده پیاده‌سازی می‌کند.

### ۲. کالبدشکافی خط به خط کد (`error_handler.py`)
* **تابع `divide(a, b)`:**
  - عملیات تقسیم دو عدد را درون بلوک `try` انجام می‌دهد.
  - در صورتی که مخرج کسر (`b`) برابر صفر باشد، استثنای `ZeroDivisionError` را شکار کرده و به جای کرش کردن برنامه، پیام متنی `"خطا: تقسیم بر صفر ممکن نیست!"` را برمی‌گرداند.
* **تابع `start_app()`:**
  - درون یک حلقه `while True` قرار دارد تا زمانی که کاربر یک تقسیم معتبر انجام ندهد، برنامه به دریافت ورودی ادامه دهد.
  - **مدیریت `ValueError`:** اگر کاربر به جای عدد صحیح، حروف یا رشته متنی وارد کند، تبدیل `int(input(...))` خطای `ValueError` صادر می‌کند که توسط بلوک `except ValueError` مدیریت شده و پیام راهنما نمایش داده می‌شود.
  - **بررسی نوع خروجی (`isinstance(res, float)`):** تنها زمانی که خروجی تابع `divide` یک عدد اعشاری معتبر (`float`) باشد (یعنی تقسیم بر صفر رخ نداده باشد)، دستور `break` اجرا شده و حلقه پایان می‌یابد.
  - **بلوک تضمین‌شده `finally`:** در پایان هر دور از چرخه (چه محاسبه موفق باشد و چه خطای ورودی یا تقسیم بر صفر رخ داده باشد)، بلوک `finally` اجرا شده و وضعیت اجرای آن مرحله را گزارش می‌دهد.

---

## 🇬🇧 Complete English Documentation

### 1. Project Overview
This repository showcases defensive programming patterns in Python by isolating arithmetic exceptions (`ZeroDivisionError`) from user-input parsing exceptions (`ValueError`) inside a self-healing interactive CLI loop.

### 2. Line-by-Line Code Breakdown (`error_handler.py`)
* **`divide(a, b)`:** Wraps division inside a `try / except ZeroDivisionError` block, returning a float on success or a descriptive error string when `b == 0`.
* **`start_app()`:**
  - Continuously prompts for integer inputs inside a `while True` loop.
  - Catches non-numeric strings via `except ValueError`.
  - Validates successful calculation using `isinstance(res, float)` before breaking out of the loop.
  - Executes the `finally` clause unconditionally on every iteration to confirm cycle completion.

---

## 🚀 How to Run / نحوه اجرا

```bash
python error_handler.py
```
