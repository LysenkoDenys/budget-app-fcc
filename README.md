# 🏦 Budget App

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project%20Status-Completed-blue?style=for-the-badge)

## 💙💛 Stand with Ukraine

## 🚀 Overview

This project is a **Python-based budget management app** that allows users to:

- Track deposits and withdrawals in different budget categories.
- Transfer money between categories.
- Display the current balance per category.
- Visualize spending with a **percentage spent bar chart**.

The main class `Category` represents a budget category with a ledger of transactions. The function `create_spend_chart(categories)` generates a visual chart of spending percentages by category.

---

## 📊 sample

<img width="256" height="566" alt="Image" src="https://github.com/user-attachments/assets/6b86d6fb-3f4f-467e-9b87-6369716268f7" />

## 🗂️ Features

- **Deposit** – Add money to a category with optional description.
- **Withdraw** – Subtract money from a category with optional description.
- **Transfer** – Move money from one category to another.
- **Check Balance** – Retrieve the current balance of a category.
- **Ledger** – Maintain a detailed transaction history for each category.
- **Spending Chart** – Print a vertical bar chart showing percentages of total spending for all categories.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/LysenkoDenys/Budget-App.git
cd Budget-App

```

## 📁 Files

<pre>
Budget-App/
├── budget_app.py # Python script with the Category class and spending chart function
├── README.md # Project documentation
└── .gitignore # Git ignore file (optional)
</pre>

## 🧻 License

This project is released under the MIT License.
You’re free to use, modify, and distribute it for personal or educational purposes.
