# Data-Efficient Machine Learning for Small Tabular Datasets  
### A Comparison Study

📄 Preprint: (Add your PDF link here)

---

## 🚀 Overview

This repository contains the full experimental pipeline, datasets, and results for the research paper:

**"Data-Efficient Machine Learning for Small Tabular Datasets: A Comparison Study"**

This project explores how machine learning models perform when trained on **small tabular datasets**, which is a common real-world problem but not well studied.

---

## 🧠 Key Findings

- Logistic Regression performs best on very small datasets (<500 samples)
- Random Forest performs best on medium datasets (1000+ samples)
- XGBoost does not consistently outperform other models
- Accuracy alone is misleading — F1-score reveals class imbalance issues
- Feature quality is more important than feature quantity

---

## 📊 Problem Statement

Most machine learning research focuses on large datasets.

This project answers:
👉 *Which model should you use when your dataset is small?*

---

## ⚙️ Models Compared

- Logistic Regression  
- Random Forest  
- XGBoost  

All models use:
- Same preprocessing  
- Same train/test split  
- Same evaluation metrics  

---

## 📦 Datasets

- Heart Disease (303 samples)
- German Credit (999 samples)
- Insurance (1338 samples)
- Credit Card Default (30,000 samples)

Domains:
- Healthcare
- Finance

---

## 🧪 Methodology

### Preprocessing
- Missing values → median imputation  
- Categorical encoding → label encoding  
- Feature scaling → StandardScaler  

### Training
- 80/20 train-test split  
- Stratified sampling  
- Random state = 42  

### Evaluation Metrics
- Accuracy  
- F1 Score  
- ROC-AUC  

---

## 📈 Results Summary

| Dataset        | Best Model           |
|---------------|--------------------|
| Heart Disease | Logistic Regression |
| German Credit | Random Forest       |
| Insurance     | Random Forest       |
| Credit Card   | Random Forest       |

---

## 📉 Core Insight

Small Data → Simple Models Win  
Medium Data → Ensemble Models Win  

---

## 🧠 Practical Recommendation

- < 500 samples → Logistic Regression  
- 1000–5000 samples → Random Forest  
- Large datasets → Consider XGBoost  

---

## 📂 Project Structure
paper 1/
│
├── datasets/ # Raw datasets
├── notebook/ # Jupyter notebooks
├── paper/ # Final PDF
├── results/ # CSV outputs
├── docs/ # Notes
├── src/ # Code


---

## 🧪 Reproducibility

Install dependencies:


pip install -r requirements.txt


Run notebooks in order:


01_explore → 03_models → 08_results → 09_tables


---

## 📊 Workflow

Raw Data → Preprocessing → Train/Test Split → Models → Evaluation → Comparison

---

## ⚠️ Limitations

- Only 4 datasets  
- Only binary classification  
- No hyperparameter tuning  
- No deep learning models  

---

## 🔮 Future Work

- Add more datasets (200–800 samples range)  
- Compare with deep learning tabular models  
- Add feature engineering  
- Extend to multi-class tasks  

---

## 📜 Paper

📄 Full Paper: (Add your PDF link)

### Citation
ghoshavik853@gmail.com,
title={Data-Efficient Machine Learning for Small Tabular Datasets: A Comparison Study},
author={Ghosh, Avik},
year={2026}
}
