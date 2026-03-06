# 💰 Tip Prediction App

A simple **Machine Learning web app** built with **Python and Streamlit** that predicts the tip amount based on restaurant bill details.

## 🚀 Live Idea

Users enter restaurant information like total bill, gender, smoker status, day, time, and size of the group.
The trained ML model predicts the **expected tip amount**.

---

## 📌 Features

* Predict restaurant **tip amount**
* Simple **Streamlit web interface**
* Uses a trained **Machine Learning model**
* Easy to run locally
* Lightweight project for ML beginners

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Scikit-learn**
* **Pickle**

---

## 📂 Project Structure

```
Tip-Prediction-App
│
├── app.py                # Streamlit application
├── tips_model.pkl        # Trained ML model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/codewithesha2002-design/Tips_prediction.git
cd Tips_prediction
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser:

```
http://localhost:8501
```

---

## 📊 Example Inputs

* Total Bill
* Gender
* Smoker (Yes/No)
* Day (Sun, Sat, etc.)
* Time (Lunch/Dinner)
* Size of group

The model predicts the **tip amount 💵**.

---

## 🧠 Machine Learning Model

The model was trained on the **restaurant tips dataset** and saved using **Pickle (`tips_model.pkl`)**.

---

## 🤝 Contributing

Contributions are welcome!
Feel free to **fork the repo** and submit a **pull request**.

---

## 👩‍💻 Author

**Esha (Kanika Sharma)**
💻 AI / ML | Full Stack Developer

GitHub:
https://github.com/codewithesha2002-design

---

⭐ If you like this project, consider **starring the repo**!
