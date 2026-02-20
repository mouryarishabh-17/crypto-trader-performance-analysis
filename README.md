# Trader Performance & Market Sentiment Analysis

## 📌 Project Overview
This project analyzes the relationship between **Bitcoin Market Sentiment (Fear & Greed Index)** and **Trader Performance** on the Hyperliquid platform. The goal is to uncover behavioral patterns and performance differences across various sentiment regimes to inform smarter trading strategies.

## 📂 Dataset
The analysis uses two datasets:
1.  **Bitcoin Fear & Greed Index (`fear_greed_index.csv`)**: Daily sentiment classification (Fear, Greed, etc.).
2.  **Historical Trader Data (`historical_data.csv`)**: Trade execution details including PnL, size, side, and timestamps.

## 🚀 Setup & Installation
1.  Ensure you have Python installed.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 📊 How to Run
1.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook analysis_notebook.ipynb
    ```
2.  Run all cells to reproduce the analysis and visualizations.

## 💡 Key Insights (Part B)
Based on the data analysis:
1.  **Fear vs. Greed Performance**:
    *   **Profitability**: Traders show significantly **higher daily PnL** during **"Fear"** periods compared to "Greed" or "Extreme Greed".
    *   **Activity**: Trading volume is drastically higher during Fear, suggesting high engagement during volatility.
2.  **Behavioral Shifts**:
    *   **Trade Size**: Average trade sizes are largest during **"Extreme Greed"** and **"Fear"**, indicating higher conviction or forced repositioning during extremes.
    *   **Directional Bias**: There is a general **Sell bias** across all sentiments, but it is most pronounced during **"Greed"** (Profit taking?).

## 🧠 Strategy Recommendations (Part C)
1.  **"Fear Volatility Harvesting"**:
    *   **Concept**: Since PnL and volume peak during Fear, allocate more capital to active trading strategies during these periods. The market volatility likely provides more actionable setups.
2.  **"Contrarian Greed Fading"**:
    *   **Concept**: During "Greed" phases, where the Sell bias is strong yet PnL is lower, adopt a defensive stance. Tighten stop-losses on Longs or look for mean-reversion Short opportunities, as the crowd might be over-leveraged.

## 📁 Files
*   `analysis_notebook.ipynb`: Main analysis code and visualizations.
*   `predictive_model.py`: Bonus script for predicting trade profitability (93% accuracy).
*   `requirements.txt`: Python dependencies.
*   `merged_data.csv`: Processed dataset.
*   `feature_importance.png`: Feature importance plot from the predictive model.

## 🤖 Bonus: Predictive Model
A Random Forest Classifier was built to predict individual trade profitability:
*   **Accuracy**: ~93%
*   **Key Drivers**: `Start Position` and `Side` were the most significant predictors of trade outcome.

