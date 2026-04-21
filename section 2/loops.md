

## 🔹 يعني إيه Loop؟

الـ Loop ببساطة = تكرار تنفيذ كود معين أكتر من مرة بدل ما تكتبه يدوي.

---

## 🔹 أنواع الـ Loops في Python

### 1️⃣ `for loop`

بتستخدمها لما تكون عارف عدد التكرار أو بتلف على list / string / range

```python
for i in range(5):
    print(i)
```

📌 الناتج:

```
0 1 2 3 4
```

💡 شرح بالمصري:
بيبدأ من 0 لحد قبل 5، ويمشي واحدة واحدة

---

### مثال عملي:

```python
names = ["Ali", "Omar", "Sara"]

for name in names:
    print(name)
```

💡 بيلف على كل عنصر في الليست

---

## 🔹 2️⃣ `while loop`

بتستخدمها لما التكرار بيعتمد على شرط

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

💡 طالما الشرط صح → كمل
لو الشرط غلط → وقف

---

## ⚠️ خلي بالك من Infinite Loop

```python
while True:
    print("Hello")
```

💀 ده هيقعد شغال للأبد (لازم break علشان توقفه)

---

## 🔹 break & continue

### ✅ break → يوقف اللوب

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

### ✅ continue → يتخطى iteration واحدة

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## 🔹 else مع loop (حاجة ناس كتير متعرفهاش 😏)

```python
for i in range(3):
    print(i)
else:
    print("خلصنا")
```

💡 الـ else بتشتغل لو اللوب خلص طبيعي (مش بـ break)

---

## 🔥 Tips مهمة ليك كمبرمج:

* استخدم `for` لما تكون بتتعامل مع list أو range
* استخدم `while` لما يكون عندك condition مش عدد محدد
* حاول دايمًا تتجنب infinite loops
* خلي الكود بسيط وواضح

---

