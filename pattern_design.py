# pattern_design.py
"""
الگوی Singleton:
این الگو تضمین می‌کند که یک کلاس تنها یک نمونه داشته باشد و یک نقطه دسترسی سراسری به آن فراهم کند.
کاربرد: مدیریت منابع مشترک مانند اتصال پایگاه داده، تنظیمات برنامه، یا لاگر.
"""
class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True

    @classmethod
    def get_instance(cls, value=None):
        if cls._instance is None:
            cls._instance = cls(value)
        return cls._instance


# --- آزمون ---
if __name__ == "__main__":
    s1 = Singleton.get_instance(10)
    s2 = Singleton.get_instance(20)
    print(s1.value)  # 10
    print(s2.value)  # 10
    print(s1 is s2)  # True