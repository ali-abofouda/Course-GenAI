
---

## ❓ يعني إيه Magic Methods؟

**(What are Magic Methods?)**

### ✅ Short Answer (EN)

Magic methods are special methods in Python (with double underscores) that define how objects behave.

---

## 💬 الشرح بالمصري

هي دوال خاصة في بايثون:

* اسمها بيبدأ وينتهي بـ `__`
* زي: `__init__`, `__str__`, `__len__`

📌 بتخلي الكلاس بتاعك يتعامل زي الـ built-in objects
(زي list / string)

---

## 🎯 الفكرة ببساطة

بدل ما بايثون يتعامل مع object بشكل عادي
انت بتقوله "يتصرف إزاي" في مواقف معينة

---

## 🔑 أشهر Magic Methods

---

## 🟢 1. `__init__` (Constructor)

```python
class Person:
    def __init__(self, name):
        self.name = name
```

💬 بيتنفذ أول ما تعمل object

---

## 🟡 2. `__str__` (للطباعة)

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"
```

```python
p = Person("Ali")
print(p)  # بدل ما يطبع object address
```

---

## 🔵 3. `__len__` (الطول)

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
```

```python
obj = MyList([1,2,3])
print(len(obj))  # 3
```

---

## 🔴 4. `__add__` (الجمع)

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
```

```python
n1 = Number(5)
n2 = Number(10)

print(n1 + n2)  # 15
```

---

## 🟣 5. `__eq__` (المقارنة)

```python
class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age
```

```python
p1 = Person(20)
p2 = Person(20)

print(p1 == p2)  # True
```

---

## ⚡ الفكرة المهمة جدًا

أي عملية زي:

* `+`
* `==`
* `len()`
* `print()`

👉 وراها Magic Method

---

## 🔥 مثال يجمع كل حاجة

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"Book with {self.pages} pages"
```

```python
b = Book(100)

print(len(b))  # 100
print(b)       # Book with 100 pages
```

---

## 🧠 الخلاصة

| الميثود    | الاستخدام    |
| ---------- | ------------ |
| `__init__` | إنشاء object |
| `__str__`  | الطباعة      |
| `__len__`  | الطول        |
| `__add__`  | الجمع        |
| `__eq__`   | المقارنة     |

---

## 🎯 الجملة المهمة

**Magic methods let your objects behave like built-in types.**

---

