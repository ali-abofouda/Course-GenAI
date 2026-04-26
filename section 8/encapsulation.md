
---

## 🔒 يعني إيه Encapsulation؟

**Encapsulation = إخفاء البيانات + التحكم في الوصول ليها**

📌 يعني:

* بنخلي البيانات (variables) جوه الـ class
* ونمنع الوصول المباشر ليها
* ونخلي التعامل يتم من خلال functions (methods)

---

## 🎯 الهدف منها

* حماية البيانات من التعديل الغلط
* تنظيم الكود
* التحكم في إزاي البيانات تتقري أو تتغير

---

## 🧠 الفكرة ببساطة

بدل ما أي حد يعدّل في المتغير مباشرة 👇

```python
obj.balance = -1000  # ❌ غلط
```

نخليه يعدي على function تتحكم 👇

```python
obj.withdraw(100)  # ✅ صح
```

---

## 🧱 مثال عملي

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("رصيد غير كافي")

    def get_balance(self):
        return self.__balance
```

---

## 🔍 شرح الكود (بالمصري)

* `__balance` → ده **private** (مخفي)
* مينفعش توصله مباشرة من برا
* لازم تستخدم methods زي:

  * `deposit()`
  * `withdraw()`
  * `get_balance()`

---

## 🧪 استخدام الكلاس

```python
acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(200)

print(acc.get_balance())  # 1300
```

❌ لو حاولت تعمل:

```python
print(acc.__balance)
```

هيطلع error

---

## ⚠️ ملاحظات مهمة

في بايثون مفيش private حقيقي 100%
لكن بنستخدم:

* `_var` → protected (اتفاق بس)
* `__var` → private (name mangling)

📌 تقدر توصل له كده (مش مستحب):

```python
print(acc._BankAccount__balance)
```

---

## 💡 الخلاصة (Short Answer بالإنجليزي)

**Encapsulation is the process of hiding internal data and allowing access only through controlled methods.**

---
