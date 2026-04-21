---

# 🧠 يعني إيه Tuple؟

الـ Tuple زي الـ List 👇
بس الفرق الأساسي:

👉 **Immutable** = مينفعش تتغير بعد ما تتعمل

---

## 🔹 تعريف Tuple

```python
t = (1, 2, 3)
names = ("Ali", "Sara", "Omar")
```

💡 ممكن كمان تكتبها من غير أقواس:

```python
t = 1, 2, 3
```

---

## ⚠️ نقطة مهمة جدًا

لو عنصر واحد بس:

```python
t = (5,)   # صح
t = (5)    # ❌ ده int مش tuple
```

---

# 🔹 الوصول للعناصر

```python
t = (10, 20, 30)

print(t[0])   # 10
print(t[-1])  # 30
```

---

# 🔹 Slicing

```python
t = (1, 2, 3, 4, 5)

print(t[1:4])  # (2, 3, 4)
```

---

# 🔹 الفرق بين List و Tuple

| الحاجة  | List      | Tuple |
| ------- | --------- | ----- |
| التعديل | ✔️ ينفع   | ❌ لا  |
| الأداء  | أبطأ شوية | أسرع  |
| الأمان  | أقل       | أعلى  |

---

# 🔹 ليه نستخدم Tuple؟

## ✅ 1. حماية البيانات

```python
point = (10, 20)
```

مش هيتغير بالغلط

---

## ✅ 2. أسرع في الأداء

(مهم في الـ data الكبيرة)

---

## ✅ 3. ينفع يكون Key في dict

```python
d = {
    (1, 2): "point"
}
```

---

# 🔹 Loop على Tuple

```python
t = (1, 2, 3)

for x in t:
    print(x)
```

---

# 🔹 unpacking (مهم جدًا 🔥)

```python
t = (1, 2, 3)

a, b, c = t

print(a)  # 1
```

---

## 🔥 Pro level:

```python
a, b, *rest = (1, 2, 3, 4, 5)

print(rest)  # [3, 4, 5]
```

---

# 🔹 دوال مهمة

```python
t = (1, 2, 2, 3)

print(len(t))     # الطول
print(t.count(2)) # عدد التكرار
print(t.index(3)) # مكان العنصر
```

---

# 🔹 تحويل بين List و Tuple

```python
t = tuple([1, 2, 3])
l = list((1, 2, 3))
```

---

# ⚠️ خد بالك

❌ مينفعش:

```python
t[0] = 10
```

لكن لو جواه list:

```python
t = ([1, 2], 3)
t[0][0] = 99  # ✔️ ينفع
```

---

# 🔥 استخدامات حقيقية

* إرجاع أكتر من قيمة من function

```python
def get_user():
    return "Ali", 21
```

* الإحداثيات (x, y)
* data ثابتة مش عايزها تتغير
* keys في dict

---

# 🧠 خلاصة:

👉 استخدم **Tuple** لما:

* البيانات ثابتة
* عايز performance أعلى
* عايز أمان

---

# 🔥 Challenge ليك

اكتب function:

* تستقبل list أرقام
* وترجع:

  * أكبر رقم
  * أصغر رقم

👉 باستخدام tuple

مثال:

```python
result = get_min_max([3, 7, 1, 9])
print(result)  # (1, 9)
```

---