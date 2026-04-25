---

# 🧠 يعني إيه Exception؟

الـ **Exception** = خطأ بيحصل وقت تشغيل البرنامج (runtime)

👉 زي:

* قسمة على صفر
* فتح ملف مش موجود
* إدخال نوع غلط

---

## 🔹 مثال:

```python
print(10 / 0)
```

💀 ده يدي:

```
ZeroDivisionError
```

---

# 🔹 التعامل مع الأخطاء (try / except)

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)
except:
    print("فيه خطأ حصل")
```

💡 البرنامج مش هيقع 👍

---

# 🔥 الأفضل (تحديد نوع الخطأ)

```python
try:
    x = int(input("Enter number: "))
    print(10 / x)

except ZeroDivisionError:
    print("مينفعش تقسم على صفر")

except ValueError:
    print("دخل رقم صح")
```

---

# 🔹 else

```python
try:
    x = int(input())
except ValueError:
    print("خطأ")
else:
    print("تمام:", x)
```

💡 `else` بيشتغل لو مفيش error

---

# 🔹 finally (مهم 👀)

```python
try:
    f = open("file.txt")
except FileNotFoundError:
    print("مش موجود")
finally:
    print("خلصنا")
```

💡 بيتنفذ في كل الحالات

---

# 🔹 التقاط كل الأخطاء

```python
try:
    x = 10 / 0
except Exception as e:
    print(e)
```

💡 `e` فيها رسالة الخطأ

---

# 🔹 raise (إنك ترمي error بنفسك 🔥)

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("رصيد غير كافي")
```

---

# 🔹 custom exception

```python
class MyError(Exception):
    pass

raise MyError("حصل خطأ خاص")
```

---

# 🔹 مثال عملي مهم

```python
while True:
    try:
        x = int(input("Enter number: "))
        break
    except ValueError:
        print("حاول تاني")
```

💡 user input safe 👌

---

# ⚠️ أخطاء شائعة

❌ تستخدم except فاضي:

```python
except:
    pass
```

👉 ده خطر (بيخبي الأخطاء)

---

❌ تمسك كل الأخطاء بدون سبب:

```python
except Exception:
```

👉 استخدمه بحذر

---

# 🔥 استخدامات حقيقية

* التعامل مع API errors
* user input validation
* file handling
* backend (🔥 مهم جدًا ليك)

---

# 🧠 خلاصة

👉 Exception = حماية البرنامج من الكراش
👉 try/except = أمان
👉 finally = تنظيف

---

# 🔥 Challenge ليك

اكتب برنامج:

* يطلب من المستخدم رقمين
* يقسمهم على بعض
* يعالج:

  * إدخال غلط
  * القسمة على صفر

👉 ويخلي المستخدم يحاول لحد ما يدخل صح

---


