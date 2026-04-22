# 🧠 يعني إيه List؟

الـ List = مجموعة عناصر في ترتيب معين
تقدر تخزن فيها أي حاجة (أرقام – نصوص – حتى Lists تانية)

```python
nums = [1, 2, 3, 4]
names = ["Ali", "Sara", "Omar"]
mixed = [1, "Ali", True]
```

---

# 🔹 الوصول للعناصر (Indexing)

```python
nums = [10, 20, 30]

print(nums[0])   # 10
print(nums[-1])  # 30
```

💡 بالمصري:

* أول عنصر index = 0
* السالب بيبدأ من الآخر

---

# 🔹 التقطيع (Slicing)

```python
nums = [1, 2, 3, 4, 5]

print(nums[1:4])  # [2, 3, 4]
print(nums[:3])   # [1, 2, 3]
print(nums[::2])  # [1, 3, 5]
```

---

# 🔹 تعديل القيم

```python
nums = [1, 2, 3]
nums[0] = 10
```

---

# 🔹 أهم الدوال (Methods)

## ➕ إضافة عناصر

```python
nums.append(4)        # يضيف في الآخر
nums.insert(1, 99)   # يضيف في مكان معين
```

---

## ❌ حذف عناصر

```python
nums.remove(2)   # يحذف بالقيمة
nums.pop()       # يحذف آخر عنصر
nums.pop(1)      # يحذف بالindex
```

---

## 🔄 ترتيب

```python
nums.sort()              # تصاعدي
nums.sort(reverse=True)  # تنازلي
```

---

## 🔍 بحث

```python
nums.index(3)   # يرجع مكان العنصر
nums.count(2)   # عدد التكرار
```

---

# 🔹 Loop على List

```python
nums = [1, 2, 3]

for n in nums:
    print(n)
```

---

## 🔥 مع index:

```python
for i, n in enumerate(nums):
    print(i, n)
```

---

# 🔹 List Comprehension (مهم جدًا 🔥)

بدل:

```python
nums = []
for i in range(5):
    nums.append(i)
```

تكتب:

```python
nums = [i for i in range(5)]
```

---

## 🎯 مع شرط:

```python
even = [i for i in range(10) if i % 2 == 0]
```

---

# 🔹 Nested List

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])  # 2
```

---

# 🔹 نسخ الـ List (مهم 👀)

```python
a = [1, 2, 3]
b = a.copy()
```

❌ غلط:

```python
b = a  # نفس المكان في الميموري
```

---

# 🔹 عمليات على List

```python
a = [1, 2]
b = [3, 4]

print(a + b)   # دمج
print(a * 3)   # تكرار
```

---

# 🔹 Check وجود عنصر

```python
if 3 in nums:
    print("yes")
```

---

# 🔥 استخدامات حقيقية

* تخزين بيانات (users, products)
* التعامل مع API responses
* بناء UI lists في Angular (🔥 مهم ليك)
* Data processing في AI

---

# ⚠️ أخطاء شائعة

❌ تعديل list أثناء loop:

```python
for i in nums:
    nums.remove(i)  # خطر
```

---

# 🧠 خلاصة سريعة:

| الحاجة        | تستخدمها امتى   |
| ------------- | --------------- |
| list          | بيانات مرتبة    |
| append        | تضيف عنصر       |
| for           | تلف على العناصر |
| comprehension | كود أقصر وأسرع  |

---

# 🔥 Challenge ليك (تقيل 😏)

اكتب برنامج:

* عنده list أرقام
* يطلع list جديدة فيها:

  * الأرقام الموجبة فقط
  * وكل رقم مضروب في 2

👉 مثال:

```text
input: [-1, 2, -3, 4]
output: [4, 8]
```