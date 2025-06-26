# RegimeRadar
#Week 1: Financial Data Feature Engineering & Visualization

## Overview

This week marked the foundation of my data analytics journey, where I learned to work with Python libraries such as:

- **NumPy**
- **Pandas**
- **Matplotlib**

The focus was on handling real-world financial data, extracting insights from order book and trade data, and building visual indicators for market analysis.

---

## 📁 Datasets Used

1. **depth20.csv** – Contains top 20 bid/ask price levels from the order book (Level 2 data).
2. **aggTrade.csv** – Contains aggregated executed trades (tick-by-tick trade history).

---

## ✅ Key Skills Gained

### 📊 Data Manipulation
- Extracted and processed structured financial data using **Pandas**.
- Handled timestamps, price-volume arrays, and calculated derived columns.

### ⚙️ Feature Engineering
Computed essential market indicators such as:
- **Spread** = Best Ask - Best Bid
- **Mid Price** = (Best Ask + Best Bid) / 2
- **Order Book Imbalance** = (Sum of Bid Volumes - Sum of Ask Volumes) / (Sum of Bid Volumes + Sum of Ask Volumes)
- **Rolling Volatility** using rolling standard deviation of mid-price returns

### 📈 Visualization
- Created time-series plots to visualize changes in spread, mid price, and volatility.
- Plotted imbalance heatmaps and volatility overlays using **Matplotlib**.

---

## 🧠 Learnings

- Understood how to represent market microstructure using order book data.
- Gained experience transforming raw tick data into meaningful indicators.
- Reinforced the importance of **data cleaning**, **window-based operations**, and **normalization** in financial data science.

---
