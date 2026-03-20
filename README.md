# Machine Learning Practice Projects

A collection of 11 mini weekly projects covering core Machine Learning concepts — from statistics and EDA to supervised and unsupervised learning — built using Python and Scikit-learn.

---

## 📦 Installation

### Prerequisites
Python 3.8+ required.

### Install all libraries at once
```bash
# Recommended way
pip install -r requirements.txt
```

### Or install individually
```bash
pip install pandas                  # Data manipulation
pip install numpy                   # Numerical computing
pip install matplotlib              # Plotting
pip install seaborn                 # Statistical visualization
pip install scikit-learn            # ML models
pip install scipy                   # Statistics & clustering
pip install xgboost                 # Gradient boosting
pip install imbalanced-learn        # SMOTE for imbalanced datasets
pip install plotly                  # Interactive charts
pip install ydata-profiling         # Auto EDA reports
pip install kagglehub               # Kaggle dataset downloader
pip install fastapi uvicorn         # Project-4 Titanic API
```

---

## 📁 Project Structure

```
Machine_learning_practice/
│
├── Mini_weekly_project-1/          # Statistics Fundamentals
│   ├── statistics_fundamentals.ipynb
│   └── student_scores.csv
│
├── Mini_weekly_project-2/          # Inferential Statistics & Probability
│   ├── inferential_statistics_probability.ipynb
│   └── Weather Data in India from 1901 to 2017.csv
│
├── Mini_weekly_project-3/          # Linear Algebra & Calculus
│   ├── linear_algebra_calculus_Intuitive.ipynb
│   └── Salary_Data.csv
│
├── Mini_weekly_project-4/          # EDA + ML Models
│   ├── titanic/
│   │   ├── titanic_dataset.ipynb
│   │   ├── model_pickel
│   │   ├── Testing_fastapi_rf/
│   │   │   ├── main.py
│   │   │   └── model_pickel_titanic_rf
│   │   └── gender_submission.csv
│   ├── black friday/
│   │   └── black_friday_dataset.ipynb
│   └── coaster/
│       ├── introduction_to_EDA_coaster.ipynb
│       ├── coaster_db.csv
│       └── output.png
│
├── Mini_weekly_project-5/          # Regression Practice
│   ├── project_week_5.ipynb
│   ├── practise.ipynb
│   ├── homeprices.csv
│   └── 500hits.csv
│
├── Mini_weekly_project-6/          # Calorie Prediction
│   └── project-6.ipynb
│
├── Mini_weekly_project-7/          # Spotify Analysis
│   ├── week_7_project_spotify.ipynb
│   ├── week-7_practise.ipynb
│   └── iris_gridsearch.pkl
│
├── Mini_weekly_project-8/          # Diabetes Classification (Naive Bayes)
│   └── diabetes_naive_bayes.ipynb
│
├── Mini_weekly_project-9/          # Disease Risk Prediction (KNN)
│   └── knn_disease_risk.ipynb
│
├── Mini_weekly_project-10/         # SVC + SVR
│   ├── SVC/
│   │   ├── banking_svc.ipynb
│   │   └── bank-additional-names.txt
│   └── SVR/
│       └── price_svr.ipynb
│
├── Mini_weekly_project-11/         # Clustering (K-Means & DBSCAN)
│   ├── K_means_clusterning_heir/
│   │   └── online_retail.ipynb
│   └── Unsupervised(DBSCAN)/
│       ├── country_data_dbscan.ipynb
│       ├── Country-data.csv
│       ├── data-dictionary.csv
│       └── Country_data_report.html
│
├── datasets.md                     # Download links for large datasets
└── README.md
```

---

## 📚 Projects Overview

| Project | Topic | Algorithms / Concepts |
|---------|-------|----------------------|
| Project-1 | Statistics Fundamentals | Mean, Median, Std Dev, Distributions |
| Project-2 | Inferential Statistics & Probability | Hypothesis Testing, Normal, Binomial, Poisson |
| Project-3 | Linear Algebra & Calculus | Matrices, Gradients, Salary Regression |
| Project-4 | EDA + ML Models | Random Forest, FastAPI, EDA, Decision Tree |
| Project-5 | Regression Practice | Linear Regression, Model Evaluation |
| Project-6 | Calorie Prediction | Regression, Feature Engineering, Scaling |
| Project-7 | Spotify Analysis | GridSearchCV, PCA, Cross Validation |
| Project-8 | Diabetes Classification | Naive Bayes, SMOTE, ROC-AUC |
| Project-9 | Disease Risk Prediction | KNN, StandardScaler, Classification Report |
| Project-10 | SVC + SVR | Support Vector Classifier, Support Vector Regressor |
| Project-11 | Clustering | K-Means, Hierarchical, DBSCAN, Silhouette Score |

---

## 📥 Datasets

Large datasets are not included in this repo due to size.
See **[datasets.md](./datasets.md)** for all download links.

Small datasets included directly in the repo:
- `student_scores.csv`
- `Weather Data in India from 1901 to 2017.csv`
- `Salary_Data.csv`
- `coaster_db.csv`
- `homeprices.csv`
- `500hits.csv`
- `gender_submission.csv`
- `Country-data.csv`
- `data-dictionary.csv`
- `bank-additional-names.txt`

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Matplotlib / Seaborn | Visualization |
| Scikit-learn | ML models, preprocessing, evaluation |
| SciPy | Statistics, clustering |
| XGBoost | Gradient boosting |
| Imbalanced-learn | SMOTE for class imbalance |
| Plotly | Interactive charts |
| YData Profiling | Auto EDA reports |
| FastAPI + Uvicorn | REST API for Titanic model |
| Pickle | Model saving and loading |

---

## 👤 Author

**Vatsal**
Weekly ML Projects
Machine Learning | Scikit-learn | Python
