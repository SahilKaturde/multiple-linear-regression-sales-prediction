# 📊 Multiple Linear Regression – Sales Prediction

A simple and interactive project that predicts **Sales** based on **TV**, **Radio**, and **Newspaper** advertising spends using **Multiple Linear Regression (MLR)**. It includes a **Streamlit web app** for real-time predictions.

## ✨ Project Badges

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Library-NumPy-blueviolet)](https://numpy.org/)
[![Streamlit](https://img.shields.io/badge/App-Streamlit-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub stars](https://img.shields.io/github/stars/SahilKaturde/multiple-linear-regression-sales-prediction?style=social)](https://github.com/SahilKaturde/multiple-linear-regression-sales-prediction/stargazers)

---

## 🧠 Overview

This project explores how advertising budgets affect sales. We trained a custom Multiple Linear Regression model, analyzed results, and visualized performance—all in one place.

---

## 🧮 Model Formula

The core idea is to model the relationship between the features ($x_i$) and the target ($y$) linearly:

$$
y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \beta_3x_3 + \epsilon
$$

| Variable | Description |
| :--- | :--- |
| $\mathbf{y}$ | Predicted Sales |
| $\mathbf{x_1, x_2, x_3}$ | TV, Radio, Newspaper Spends |
| $\mathbf{\beta_0, \beta_i}$ | Model Intercept and Coefficients |

The model is trained using the **Normal Equation** method, which calculates the optimal weights ($\theta$) analytically:

$$
\theta = (X^T X)^{-1} X^T y
$$

---

## 📂 Project Structure
