
---

## ❓ يعني إيه Operator Overloading؟

**(What is Operator Overloading?)**

### ✅ Short Answer (EN)

Operator overloading allows you to redefine how operators work for objects.

---

## 💬 الشرح بالمصري

ببساطة:

* تخلي الـ operators زي `+ - ==`
* تشتغل بطريقتك على الـ objects

📌 يعني بدل ما `+` يجمع أرقام بس
تخليه يجمع objects انت عاملها

---

## 🎯 الفكرة

بايثون أصلاً بيستخدم:

* `+` → وراها `__add__`
* `==` → وراها `__eq__`

👉 انت بتغير السلوك ده

---

## 🧱 مثال بسيط

```python id="sg1bq2"
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
```

---

## 🧪 الاستخدام

```python id="3tdx02"
n1 = Number(10)
n2 = Number(5)

print(n1 + n2)  # 15
```

💬 هنا:
`n1 + n2` → بتتنفذ كده:

```python id="dzyczb"
n1.__add__(n2)
```

---

## 🔥 مثال أقوى (Vector)

```python id="r8n7k7"
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
```

---

## 🧪 الاستخدام

```python id="e60gb5"
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2
print(v3)  # (4, 6)
```

---

## 🔁 أهم Operators + الميثود بتاعتها

| Operator | Magic Method  |
| -------- | ------------- |
| `+`      | `__add__`     |
| `-`      | `__sub__`     |
| `*`      | `__mul__`     |
| `/`      | `__truediv__` |
| `==`     | `__eq__`      |
| `<`      | `__lt__`      |

---

## ⚠️ نقطة مهمة

لازم تتأكد:

* إن `other` نفس النوع
* أو تعمل validation

مثال:

```python id="wzsm2g"
def __add__(self, other):
    if isinstance(other, Vector):
        return Vector(self.x + other.x, self.y + other.y)
    return "Invalid operation"
```

---

## 🎯 الفرق بينه وبين Magic Methods

* Magic Methods → الأدوات (`__add__`)
* Operator Overloading → الاستخدام

---

## 🧠 الخلاصة

* بتغير سلوك operators
* باستخدام magic methods
* بتخلي الكود أبسط وأقرب للطبيعي

---

## 💡 جملة مهمة

**Operator overloading makes your objects behave like real-world entities.**

---

