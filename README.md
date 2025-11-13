```markdown
# 📊 Multiple Linear Regression – Sales Prediction

A simple and interactive project that predicts **Sales** based on **TV**, **Radio**, and **Newspaper** advertising spends using **Multiple Linear Regression (MLR)**. It includes a **Streamlit web app** for real-time predictions.

## ✨ Project Badges

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub stars](https://img.shields.io/github/stars/SahilKaturde/multiple-linear-regression-sales-prediction?style=social)](https://github.com/SahilKaturde/multiple-linear-regression-sales-prediction/stargazers)

---

## 🧠 Overview & Model

This project uses a custom-implemented Multiple Linear Regression model, trained via the **Normal Equation**, to analyze how advertising budgets affect product sales.

### Model Formula (Normal Equation)

The model finds the optimal coefficients ($\theta$) by:

$$
\theta = (X^T X)^{-1} X^T y
$$

Where $y$ (Sales) is a linear function of $x_1$ (TV), $x_2$ (Radio), and $x_3$ (Newspaper).

---

## ⚙️ Tech Stack

| Category | Tools |
| :--- | :--- |
| **Language** | Python 🐍 |
| **Data & Math** | NumPy, Pandas |
| **Visualization** | Matplotlib |
| **Deployment** | Streamlit |

---

## 📂 Project Structure

```

Multiple Linear Regression (Sales Prediction)/
├── app/
│   ├── mlr\_model.py         \# Custom MLR class
│   ├── work.py              \# Streamlit web app
│   └── model.pkl            \# Trained model file
├── notebooks/
│   └── EDA\_and\_Model.ipynb  \# Training and analysis notebook
├── dataset/
│   └── advertising.csv      \# Dataset
├── screenshot/
│   └── ...                  \# Visuals
└── README.md

````

---

## 📈 Visuals

### Actual vs Predicted Sales
This plot shows model accuracy. Points close to the red dashed line ($y=x$) indicate perfect predictions.
![Actual vs Predicted](screenshot/actual_vs_predicted.png)

### Streamlit Application
Screenshot of the interactive prediction interface.
![Streamlit App](screenshot/screen_shot.png)

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SahilKaturde/multiple-linear-regression-sales-prediction.git](https://github.com/SahilKaturde/multiple-linear-regression-sales-prediction.git)
   cd multiple-linear-regression-sales-prediction
````

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**

    ```bash
    streamlit run app/work.py
    ```

    The application will open automatically in your browser (usually at `http://localhost:8501`).

-----

