---

# 🧠 يعني إيه Function؟

الـ function = **قطعة كود ليها اسم** بتعمل مهمة معينة وتقدر تعيد استخدامها بدل ما تكرر الكود

---

## 🔹 تعريف function

```python
def greet():
    print("Hello")
```

📌 الاستخدام:

```python
greet()
```

---

# 🔹 Function فيها parameters

```python
def greet(name):
    print("Hello", name)

greet("Ali")
```

💡 `name` = parameter
💡 `"Ali"` = argument

---

# 🔹 return (مهم جدًا 🔥)

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

💡 الفرق:

* `print` → يطبع بس
* `return` → يرجع قيمة تستخدمها بعد كده

---

# 🔹 default parameters

```python
def greet(name="User"):
    print("Hello", name)

greet()        # Hello User
greet("Ali")   # Hello Ali
```

---

# 🔹 keyword arguments

```python
def info(name, age):
    print(name, age)

info(age=21, name="Ali")
```

---

# 🔹 args و kwargs 🔥

## args → عدد غير محدود من القيم

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))
```

---

## kwargs → key:value

```python
def user_info(**kwargs):
    print(kwargs)

user_info(name="Ali", age=21)
```

---

# 🔹 return أكتر من قيمة (tuple 👀)

```python
def calc(a, b):
    return a+b, a-b

x, y = calc(5, 3)
```

---

# 🔹 type hints (احترافي 👨‍💻)

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

# 🔹 docstring (شرح function)

```python
def add(a, b):
    """جمع رقمين"""
    return a + b
```

---

# 🔹 scope (مهم جدًا 👀)

## local:

```python
def test():
    x = 10
```

## global:

```python
x = 5

def test():
    print(x)
```

---

# 🔹 lambda function (سريعة 🔥)

```python
add = lambda a, b: a + b
print(add(3, 5))
```

---

# 🔹 nested function

```python
def outer():
    def inner():
        print("inside")
    inner()
```

---

# 🔹 recursion (تقيل شوية 😏)

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```

---

# 🔹 functions مع list

```python
def get_even(nums):
    return [i for i in nums if i % 2 == 0]
```

---

# 🔹 functions مع dict

```python
def count_chars(text):
    d = {}
    for ch in text:
        d[ch] = d.get(ch, 0) + 1
    return d
```

---

# 🔥 Best Practices

* اسم function يكون واضح
* كل function تعمل حاجة واحدة
* استخدم `return` بدل print
* قلل التكرار (DRY)

---

# ⚠️ أخطاء شائعة

❌ نسيان return:

```python
def add(a, b):
    a + b
```

---

❌ تعديل global بدون قصد

---

# 🔥 استخدامات حقيقية

* API functions
* backend logic (🔥 مهم ليك)
* data processing
* reusable UI logic

---

# 🧠 خلاصة

👉 function = تنظيم + إعادة استخدام + احترافية

---

# 🔥 Challenge ليك (تقيل 😏)

اكتب function:

### اسمها:

`analyze_numbers`

### تاخد:

list أرقام

### ترجع:

* عدد الأرقام
* مجموعهم
* أكبر رقم
* أصغر رقم

👉 في شكل tuple

---

## 🎯 مثال:

```python
result = analyze_numbers([3, 7, 1, 9])

print(result)
# (4, 20, 9, 1)
```

---
