---

# 🧬 يعني إيه Inheritance (الوراثة)؟

الـ Inheritance هو إنك تعمل **Class جديد ياخد كل خصائص Class تاني**
بدل ما تكتب الكود من الأول 💡

📌 يعني:
كلاس "الاب" → **Parent**
كلاس "الابن" → **Child**

---

# 🎯 الفكرة ببساطة

بدل ما تكرر الكود 👇

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
```

❌ كده كررت `name`

---

# ✅ الحل باستخدام Inheritance

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)
```

```python
class Student(Person):   # 👈 ورثنا من Person
    def __init__(self, name, grade):
        super().__init__(name)  # 👈 استدعاء الأب
        self.grade = grade
```

---

# 💡 شرح أهم النقاط

## 1. الوراثة

```python
class Student(Person):
```

يعني Student بياخد كل حاجة من Person

---

## 2. `super()`

```python
super().__init__(name)
```

دي بتستخدم علشان:

* تنادي Constructor بتاع الأب
* توفر عليك إعادة الكود

---

## 🚀 استخدام الكود

```python
s1 = Student("Ali", "A")

s1.greet()      # من الأب
print(s1.grade) # من الابن
```

---

# 🔥 أنواع Inheritance (ببساطة)

## 1. Single Inheritance

كلاس واحد يرث من كلاس واحد

```python
class A:
    pass

class B(A):
    pass
```

---

## 2. Multiple Inheritance

كلاس يرث من أكتر من كلاس

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

---

## 3. Multilevel Inheritance

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

---

# ⚡ Override (تعديل دالة الأب)

ممكن تغير سلوك دالة جاية من الأب 👇

```python
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hi from student")
```

---

# 🧠 امتى تستخدم Inheritance؟

استخدمها لما:

* عندك Classes بينهم علاقة (is-a)

  * Student is a Person
  * Doctor is a Person
* عايز تقلل تكرار الكود

---

# 🧩 الخلاصة

| المفهوم     | المعنى                    |
| ----------- | ------------------------- |
| Inheritance | كلاس ياخد خصائص كلاس تاني |
| Parent      | الكلاس الأساسي            |
| Child       | الكلاس اللي بيورث         |
| super()     | استدعاء الأب              |
| Override    | تعديل سلوك دالة           |

---

# 🔥 مثال مرتبط بمشروعك (Hotel System)

```python
class User:
    def __init__(self, name):
        self.name = name

class Customer(User):
    def book(self):
        print(self.name, "booked a hotel")

class Admin(User):
    def manage(self):
        print(self.name, "managing system")
```

---