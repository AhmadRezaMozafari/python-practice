def is_prime(n: int) -> bool:
    # اعداد کوچکتر از ۲ اول نیستند
    if n < 2:
        return False
    
    # عدد ۲ اول است
    if n == 2:
        return True
    
    # اعداد زوج بزرگتر از ۲ اول نیستند (بهینه‌سازی سریع)
    if n % 2 == 0:
        return False
    
    # فقط اعداد فرد را از ۳ تا ریشه‌ی دوم n بررسی می‌کنیم
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # گام ۲ برای رد شدن از اعداد زوج
    
    return True