📊YouTube Revenue Prediction – Machine Learning Project

Predict YouTube video ad-revenue using ML with Streamlit Deployment

📌 **Project Overview**

This project aims to **predict YouTube Ad Revenue** based on video-level performance metrics such as:

* Views
* Likes
* Comments
* Subscribers
* Engagement Rate
* Watch Time per View
* Category
* Device
* Country

The project follows a full **end-to-end machine learning pipeline**, including:

✔ Data Cleaning
✔ Exploratory Data Analysis
✔ Feature Engineering
✔ Encoding Categorical Columns
✔ Model Training
✔ Saving Model using Joblib
✔ Building Interactive Streamlit App
✔ Dynamic Currency Conversion (₹ for India / $ for other countries)

---

## 🧠 **Machine Learning Pipeline**

### ### **1️⃣ Data Cleaning**

* Removed duplicates
* Handled missing values
* Dropped unnecessary columns (`video_id`)
* Converted datatypes into numerical
* Fixed inconsistent categories
* Normalized numeric columns

### **2️⃣ Feature Engineering**

Performed:

* Engagement Rate Calculation
* Watch Time Per View
* Dropped irrelevant identifiers
* OneHotEncoding for Category, Device, Country
* Scaling numerical features

### **3️⃣ Model Building**

Trained multiple models:

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

Final model selected:

### ⭐ **Random Forest Regressor (Best Accuracy)**

Model saved using:

```
joblib.dump(model, "best_youtube_model.joblib")
```

---

## 🎯 **Prediction Factors**

The model predicts revenue using:

| Feature         | Description               |
| --------------- | ------------------------- |
| views           | Total views of the video  |
| likes           | Number of likes           |
| comments        | User comments             |
| subscribers     | Channel subscriber count  |
| engagement_rate | Likes + Comments / Views  |
| watch_per_view  | Avg watch time per viewer |
| category        | Video category            |
| device          | User device type          |
| country         | Viewer country            |

---

## 🌍 **Dynamic Currency Conversion**

| Country    | Symbol   |
| ---------- | -------- |
| India (IN) | ₹ Rupees |
| Others     | $ USD    |

Revenue is shown accordingly:

```
₹ 5,640.23 (India)
$ 342.55 (USA/UK etc.)
```

---

## 🖥 **Streamlit App Flow**

User inputs values in a web UI built using Streamlit.
Once the "Predict Revenue" button is clicked:

1. Inputs collected
2. Converted into DataFrame
3. Passed to ML model
4. Predicted revenue displayed with correct currency

---

## 🚀 **How to Run Locally**

### **1️⃣ Create Virtual Environment**

```bash
python -m venv venv
```

### **2️⃣ Activate Environment**

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Run Streamlit App**

```bash
streamlit run youtube_app.py
```

---

## 📁 **Project Structure**

```
Youtube-Revenue-Prediction/
│
├── data/
│   └── youtube_cleaned.csv
│
├── model/
│   ├── best_youtube_model.joblib
│
├── notebooks/
│   └── youtube_model_building.ipynb
│
├── youtube_app.py
├── requirements.txt
└── README.md
```

---

## 🧪 **Technologies Used**

| Category      | Tools                      |
| ------------- | -------------------------- |
| Programming   | Python                     |
| Data          | Pandas, NumPy              |
| Visualization | Matplotlib, Seaborn        |
| ML            | Scikit-Learn, RandomForest |
| Deployment    | Streamlit                  |
| Model Saving  | Joblib                     |

---

## 🎨 **Streamlit UI Preview**

* Clean Dark Theme
* User Input Controls
* Instant Prediction
* Revenue Shown with Currency
* Simple & Beginner-Friendly UI

---

## 📦 **Sample Input**

| Feature         | Value     |
| --------------- | --------- |
| views           | 45000     |
| likes           | 3200      |
| comments        | 400       |
| engagement_rate | 0.18      |
| watch_per_view  | 8.5       |
| category        | Education |
| device          | Mobile    |
| country         | IN        |

**Output Example:**

```
Predicted Revenue: ₹ 3,210.45
```

---

## 🏁 **Final Output Screenshot**

<img width="1600" height="729" alt="image" src="https://github.com/user-attachments/assets/fb785e9d-62fb-4a50-9b4f-3ea94251dc31" />
<img width="1600" height="796" alt="image" src="https://github.com/user-attachments/assets/8c251413-818f-43f5-bbd1-651dddaae8b6" />


---

## 🙌 **Author**

**Mohammed Ansari**
Beginner Machine Learning & Data Science Enthusiast.

---

## ⭐ **If you like this project — give it a star on Github!**.

