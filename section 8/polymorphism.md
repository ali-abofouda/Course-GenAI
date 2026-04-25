
---

# 🧠 يعني إيه Polymorphism؟

**Polymorphism = تعدد الأشكال**

📌 يعني:

> نفس الاسم (method/function) بس **بيتصرف بشكل مختلف حسب الكلاس**

---

# 🎯 الفكرة ببساطة

عندك دالة اسمها `speak()`
لكن:

* الكلب 🐶 ينبح
* القطة 🐱 تموء

نفس الاسم… سلوك مختلف 👌

---

# 🧾 مثال عملي

```python
class Dog:
    def speak(self):
        print("Woof 🐶")

class Cat:
    def speak(self):
        print("Meow 🐱")
```

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

---

## ✅ الناتج:

```
Woof 🐶
Meow 🐱
```

---

# 💡 ليه ده Polymorphism؟

لأن:

* استخدمنا نفس الدالة `speak()`
* لكن كل object نفذها بطريقة مختلفة

---

# 🔥 أنواع Polymorphism في بايثون

---

## 1. Method Overriding (الأهم)

يعني الكلاس الابن يغير سلوك الأب 👇

```python
class Person:
    def role(self):
        print("I am a person")

class Student(Person):
    def role(self):
        print("I am a student")
```

```python
p = Person()
s = Student()

p.role()  # I am a person
s.role()  # I am a student
```

---

## 2. Duck Typing 🦆 (ميزة جامدة في بايثون)

📌 الفكرة:

> "لو بيمشي زي البطة وبيصوّت زيها → يبقى بطة"

```python
class Car:
    def move(self):
        print("Car is moving")

class Plane:
    def move(self):
        print("Plane is flying")
```

```python
for obj in [Car(), Plane()]:
    obj.move()
```

✔ بايثون مش مهتم بالكلاس
المهم إن فيه `move()`

---

## 3. Built-in Polymorphism

زي:

```python
print(len("Ali"))       # 3
print(len([1,2,3,4]))   # 4
```

📌 نفس `len()`
لكن بيشتغل مع أنواع مختلفة

---

# 🚀 مثال مرتبط بمشروعك (Hotel System)

```python
class User:
    def dashboard(self):
        print("User Dashboard")

class Admin(User):
    def dashboard(self):
        print("Admin Dashboard")

class Customer(User):
    def dashboard(self):
        print("Customer Dashboard")
```

```python
users = [Admin(), Customer()]

for u in users:
    u.dashboard()
```

---

# 🧩 الخلاصة

| المفهوم      | المعنى                    |
| ------------ | ------------------------- |
| Polymorphism | نفس الميثود بس سلوك مختلف |
| Overriding   | تغيير دالة الأب           |
| Duck Typing  | المهم السلوك مش النوع     |
| الفايدة      | كود مرن وقابل للتوسيع     |

---

# 🔥 الخلاصة التقيلة

> Polymorphism يخليك تكتب كود عام
> والكلاسات تحدد التنفيذ بنفسها

---
