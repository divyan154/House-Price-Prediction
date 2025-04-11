# 🏡 House Price Prediction

This is a simple machine learning project that predicts house prices using the classic **Boston Housing Dataset**. The project was originally built in a Google Colab notebook and has been organized here with explanations and a clean structure.

---

## 📊 Dataset

- The dataset is sourced from the **StatLib repository at Carnegie Mellon University**:  
  [http://lib.stat.cmu.edu/datasets/boston](http://lib.stat.cmu.edu/datasets/boston)
  
- It contains **506 rows** and **13 features** plus one target column (`price`).

- Features include:
  - `CRIM`: Crime rate by town
  - `ZN`: Proportion of residential land zoned
  - `INDUS`: Proportion of non-retail business acres
  - `CHAS`: Charles River dummy variable
  - `NOX`: Nitric oxide concentration
  - `RM`: Average number of rooms per dwelling
  - `AGE`: Proportion of units built before 1940
  - `DIS`: Distance to employment centers
  - `RAD`: Index of accessibility to highways
  - `TAX`: Property tax rate
  - `PTRATIO`: Pupil-teacher ratio
  - `B`: Proportion of Black residents
  - `LSTAT`: % lower status of the population
  - `price`: Median value of owner-occupied homes (target)

---

## 🛠️ Technologies Used

- Python 🐍
- Libraries:
  - `numpy`, `pandas`
  - `matplotlib`, `seaborn`
  - `scikit-learn`
  - `xgboost`

---

## 🧪 Model Used

- **XGBoost Regressor**:
  - Chosen for its performance on tabular data
  - Easy to tune and interpret
  - Usually gives better results than linear models

---

## 📈 Evaluation Metrics

- **R² Score**
- **Mean Absolute Error**
- **Mean Squared Error**
- Feature importance visualization

---

## 🧾 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the notebook or use Python scripts:
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook notebook/House_price_prediction.ipynb
     ```
   - Or convert code into a `.py` script using `src/` modules.

---

## 📂 Project Structure

```
house-price-prediction/
│   House_price_prediction.ipynb      <- Original Colab notebook
│
├── src/
│   ├── data_loader.py                    <- Dataset loading script
│                         <- Model training & evaluation
│   
│
├── data/
│   └── README.md                         <- Dataset explanation
│
├── requirements.txt                      <- Dependencies
└── README.md                            
```

---

## 🙌 Acknowledgements

- Dataset: [StatLib at CMU](http://lib.stat.cmu.edu/datasets/boston)
- Inspired by classic ML tutorials and scikit-learn documentation.

