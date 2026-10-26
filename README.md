<div dir='rtl'>
# Python Practice

تمرین های پایتون: حلقه ها،توابع،دیکشنری،شرطها،لیست،خطاها، sqlite3و تست با pytest

## پیشنیازها

- Python 3.10+
- pytest

## نصب

```bash
pip install pytest
```

## اجرای تست ها
```bash
pytest -v 
```
## ساختار

- `practice/`— تمرین های پایه
- `prime/` — تابع is_prime و تستها
- `test_analyze/` — تابع analyze و تست ها
- `db.py` — توابع sqlite3

## چی یادگرفتم
- نوشتن توابع قابل تست با type hint 
- استفاده از pytest برای تست واحد
- عملیات پایه CRUD با SQLite3