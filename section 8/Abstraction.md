
---

## ❓ يعني إيه Abstraction؟

**(What is Abstraction?)**

### ✅ Short Answer (EN)

Abstraction is hiding implementation details and showing only essential features.

---

## 💬 الشرح بالمصري

يعني:

* توري المستخدم **هو يعمل إيه**
* وتخبي عنه **إزاي بيحصل**

📌 مثال بسيط:

* بتسوق عربية 🚗
* بتدوس بنزين → العربية تمشي
* مش محتاج تعرف الموتور شغال إزاي

👉 ده Abstraction

---

## 🎯 الفرق بينها وبين Encapsulation

* **Encapsulation** → حماية البيانات
* **Abstraction** → إخفاء التعقيد

---

## 🧱 إزاي نطبق Abstraction في بايثون؟

باستخدام:

* module اسمه: abc module
* و `abstract class`

---

## 🧩 مثال عملي

```python
from abc import ABC, abstractmethod

class Shape(ABC):  # abstract class
    @abstractmethod
    def area(self):
        pass
```

---

## 💬 الشرح

* `Shape` → كلاس عام (مش بيتعمل منه object)
* `area()` → مجرد تعريف (من غير تنفيذ)

📌 أي كلاس يرث منه لازم يطبق `area`

---

## 🔥 تطبيق عملي

```python
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r
```

---

## 🧪 الاستخدام

```python
s = Square(4)
c = Circle(3)

print(s.area())  # 16
print(c.area())  # 28.26
```

---

## ⚠️ نقطة مهمة

❌ مينفعش تعمل:

```python
shape = Shape()  # error
```

---

## 🎯 الفكرة الأساسية

انت بتقول:

> "أي Shape لازم يكون عنده area"
> بس مش بتحدد إزاي

---

## 💡 مثال من الحياة

* ATM Machine 💳
* تضغط "سحب فلوس"
* مش محتاج تعرف البنك بيعمل إيه جوه

👉 ده Abstraction

---

## 🔥 الخلاصة

| المفهوم     | المعنى                            |
| ----------- | --------------------------------- |
| Abstraction | إخفاء التفاصيل                    |
| الهدف       | تقليل التعقيد                     |
| الأداة      | abstract class + abstract methods |

---

## 🧠 جملة تحفظها

**Abstraction focuses on what to do, not how to do it.**

---

