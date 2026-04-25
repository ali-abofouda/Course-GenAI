---

## 🧠 يعني إيه Class و Object في بايثون؟

### 🔹 أولًا: الـ Class (الكلاس)

الكلاس هو **Blueprint (مخطط)** أو قالب بنحدد فيه:

* البيانات (Attributes)
* الوظائف (Methods)

يعني زي "تصميم" لعربية 🚗

---

### 🔹 ثانيًا: الـ Object (الأوبجكت)

الأوبجكت هو **نسخة فعلية من الكلاس**

يعني العربية نفسها اللي بتمشي في الشارع 👌

---

## 🧾 مثال بسيط

```python
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def drive(self):
        print(self.name, "is driving 🚗")
```

---

## 💡 نشرح الكود

### 1. تعريف الكلاس

```python
class Car:
```

كده عملنا قالب اسمه Car

---

### 2. الدالة `__init__`

```python
def __init__(self, name, color):
```

دي اسمها **Constructor**

* بتشتغل أول ما تعمل object
* بتحدد البيانات الأساسية

---

### 3. `self`

دي أهم نقطة 👇
`self` يعني: الأوبجكت الحالي

---

### 4. Attributes (البيانات)

```python
self.name = name
self.color = color
```

---

### 5. Method (function جوه الكلاس)

```python
def drive(self):
```

---

## 🚀 إنشاء Object

```python
car1 = Car("BMW", "Red")
car2 = Car("Toyota", "Blue")
```

---

## 🎯 استخدام الأوبجكت

```python
print(car1.name)     # BMW
print(car2.color)    # Blue

car1.drive()         # BMW is driving 🚗
```

---

## ⚡ مثال تاني (واقعي أكتر)

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def info(self):
        print("Name:", self.name)
        print("Grade:", self.grade)
```

```python
s1 = Student("Ali", "A")
s1.info()
```

---

## 🧩 الخلاصة

| المفهوم  | المعنى                         |
| -------- | ------------------------------ |
| Class    | قالب (Template)                |
| Object   | نسخة من الكلاس                 |
| **init** | دالة بتشتغل أول ما تنشئ object |
| self     | بيمثل الأوبجكت الحالي          |
| Method   | function جوه الكلاس            |

---

## 🔥 نصيحة مهمة ليك كمبرمج

الـ OOP (Object-Oriented Programming) بيخليك:

* تنظم الكود
* تعيد استخدامه
* تبني مشاريع كبيرة بسهولة

---

لو حابب 👇
أديك:

* تمارين تدريب 🔥
* أو مشروع صغير تستخدم فيه Classes (زي نظام حجز فنادق اللي بتعمله)

قولّي 👍
