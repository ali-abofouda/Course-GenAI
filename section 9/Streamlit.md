
---

## 💡 يعني إيه Streamlit ؟

هو **Framework في بايثون** بيخليك تعمل Web Apps (مواقع/داشبورد) بسرعة جدًا بدون ما تحتاج HTML أو CSS أو JavaScript.

👉 مناسب جدًا لـ:

* مشاريع **Machine Learning / AI**
* Dashboard (عرض بيانات)
* Tools سريعة (زي calculator أو analyzer)

---

## 🚀 ليه تستخدم Streamlit؟

* سهل جدًا (كود بايثون بس)
* سريع في التنفيذ
* مناسب لمشاريع التخرج (زي مشروعك AI Agent 👀)
* فيه Widgets جاهزة (buttons - inputs - charts)

---

## 📦 التثبيت

افتح التيرمنال واكتب:

```bash
pip install streamlit
```

---

## ▶️ تشغيل المشروع

لو عندك ملف اسمه `app.py`:

```bash
streamlit run app.py
```

لازم تكتب `run` بعد `streamlit`

---

## 🧠 مثال بسيط (أول App)

```python
import streamlit as st

st.title("Welcome Ali 👋")
st.write("ده أول تطبيق باستخدام Streamlit")

name = st.text_input("اكتب اسمك")

if name:
    st.success(f"أهلاً يا {name} 🔥")
```

---

## 🧩 أهم الـ Widgets

### 1. إدخال بيانات

```python
st.text_input("Name")
st.number_input("Age")
st.selectbox("Choose", ["A", "B", "C"])
```

---

### 2. Buttons

```python
if st.button("Click Me"):
    st.write("تم الضغط ✅")
```

---

### 3. عرض بيانات

```python
st.write("Hello")
st.success("نجاح")
st.error("خطأ")
st.warning("تحذير")
```

---

### 4. صور وفيديو

```python
st.image("image.png")
st.video("video.mp4")
```

---

### 5. Charts (مهم جدًا)

```python
import pandas as pd

data = pd.DataFrame({
    "x": [1,2,3],
    "y": [10,20,30]
})

st.line_chart(data)
```

---

## 🔥 مثال عملي ليك (AI Diagnosis UI بسيط)

```python
import streamlit as st

st.title("Medical Assistant 🩺")

symptom = st.text_area("اكتب الأعراض")

if st.button("تشخيص"):
    if symptom:
        st.warning("⚠️ ده مش تشخيص حقيقي")
        st.write("الأعراض قد تشير إلى مشكلة محتاجة دكتور")
```

---

## 🎯 تستخدمه إزاي في مشروعك؟

بما إنك شغال على:

* AI Agent
* Diagnosis System

تقدر تستخدمه في:

* UI لرفع التحاليل
* إدخال الأعراض
* عرض النتيجة
* Chat مع AI

---

## ⚡ نصايح احترافية

* استخدم `st.columns()` عشان تعمل Layout احترافي
* استخدم `st.sidebar` للـ menu
* أضف CSS عشان شكل UI يبقى جامد 🔥
* اربطه مع API (Flask / FastAPI)

---

## 🧠 الخلاصة

Streamlit =
👉 أسرع طريقة تعمل بيها Web App بالبايثون
👉 مناسب جدًا لمشروعك
👉 سهل + قوي

---

