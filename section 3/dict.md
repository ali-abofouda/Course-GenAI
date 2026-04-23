---

# 🧠 يعني إيه dict؟

الـ dict = **key : value**

👉 كل قيمة ليها مفتاح (زي JSON بالظبط)

```python
user = {
    "name": "Ali",
    "age": 21,
    "is_admin": True
}
```

---

# 🔹 الوصول للقيم

```python
print(user["name"])  # Ali
```

⚠️ لو المفتاح مش موجود → error

---

## 🔥 الحل الأفضل:

```python
print(user.get("name"))       # Ali
print(user.get("email"))      # None
print(user.get("email", "N/A"))
```

💡 بالمصري:
`get` آمن، مش هيكسر البرنامج

---

# 🔹 إضافة وتعديل

```python
user["age"] = 22      # تعديل
user["email"] = "ali@gmail.com"  # إضافة
```

---

# 🔹 حذف

```python
user.pop("age")   # حذف بالمفتاح
del user["name"]
```

---

# 🔹 Loop على dict

## keys بس:

```python
for key in user:
    print(key)
```

---

## values:

```python
for value in user.values():
    print(value)
```

---

## الاتنين مع بعض 🔥:

```python
for key, value in user.items():
    print(key, value)
```

---

# 🔹 Check وجود key

```python
if "name" in user:
    print("exists")
```

---

# 🔹 دوال مهمة

```python
len(user)        # عدد العناصر
user.keys()      # كل المفاتيح
user.values()    # كل القيم
user.items()     # key + value
```

---

# 🔹 Nested dict

```python
users = {
    "user1": {"name": "Ali", "age": 21},
    "user2": {"name": "Sara", "age": 22}
}

print(users["user1"]["name"])
```

---

# 🔹 dict comprehension 🔥

```python
nums = {i: i*i for i in range(5)}
```

💡 الناتج:

```python
{0:0, 1:1, 2:4, 3:9, 4:16}
```

---

# 🔹 مثال عملي مهم

## عد الحروف (اللي عملناه 👇)

```python
text = "hello"

count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)
```

---

# 🔹 merge dict

```python
a = {"x": 1}
b = {"y": 2}

c = a | b   # Python 3.9+
```

---

# 🔹 الفرق بين dict و list

| الحاجة    | dict            | list         |
| --------- | --------------- | ------------ |
| الوصول    | سريع جدًا (key) | بالindex     |
| الشكل     | key:value       | عناصر بس     |
| الاستخدام | بيانات منظمة    | بيانات مرتبة |

---

# 🔥 استخدامات حقيقية

* API responses (🔥 مهم جدًا ليك)
* user data
* caching
* configs
* AI / data processing

---

# ⚠️ أخطاء شائعة

❌ استخدام key مش hashable:

```python
d = {
    [1, 2]: "error"  # ❌
}
```

✔️ الصح:

```python
d = {
    (1, 2): "ok"
}
```

---

# 🧠 خلاصة

👉 استخدم dict لما:

* عندك بيانات ليها أسماء (name, age, id)
* عايز توصل بسرعة
* شغال بـ API أو JSON

---

# 🔥 Challenge ليك (تقيل 😏)

عندك list زي دي:

```python
students = [
    {"name": "Ali", "grade": 80},
    {"name": "Sara", "grade": 90},
    {"name": "Omar", "grade": 80}
]
```

### المطلوب:

اعمل dict يكون فيه:

* المفتاح = الدرجة
* القيمة = list بأسماء الطلاب

👉 الناتج:

```python
{
  80: ["Ali", "Omar"],
  90: ["Sara"]
}
```

---
