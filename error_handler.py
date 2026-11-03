def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "خطا: تقسیم بر صفر ممکن نیست!"


def start_app():
    while True:
        try:
            num1 = int(input("عدد اول را وارد کنید: "))
            num2 = int(input("عدد دوم را وارد کنید: "))

            res = divide(num1, num2)
            print("نتیجه:", res)

            if isinstance(res, float):
                break

        except ValueError:
            print("خطا: لطفاً فقط عدد وارد کنید (مثلاً hello معتبر نیست).")

        finally:
            print("برنامه با موفقیت (در این مرحله) اجرا شد!")


if __name__ == "__main__":
    start_app()
