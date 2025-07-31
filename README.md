# RegimeRadar
# Financial Data Analysis & Feature Engineering – Progress Summary

## Overview

This project is part of my ongoing learning in financial data analytics, with a focus on order book and trade data. The work is divided into weekly milestones to progressively build skills in data handling, feature engineering, and market indicator visualization.

---

## 📅 Weekly Progress

### ✅ Week 1: Learning Core Python Libraries

During the first week, I focused on building foundational skills with the following Python libraries:

- **NumPy** – for numerical computations and array operations
- **Pandas** – for data manipulation and analysis
- **Matplotlib** – for basic data visualization

These tools form the base for working with structured financial datasets, especially time-series data like order books and trades.

---

### ✅ Week 2: Financial Feature Engineering & Visualization

In Week 2, I applied the knowledge gained to real financial datasets:

#### 📁 Datasets Used
1. **depth20.csv** – Contains snapshots of the top 20 bid and ask price levels (Level 2 order book).
2. **aggTrade.csv** – Contains aggregated trade data (executed market orders).

#### 🛠 Feature Engineering Performed
- **Spread** = Best Ask - Best Bid
- **Mid Price** = (Best Ask + Best Bid) / 2
- **Order Book Imbalance** = (Sum of Bid Volumes - Sum of Ask Volumes) / (Sum of Bid Volumes + Sum of Ask Volumes)
- **Rolling Volatility** = Standard deviation of mid-price returns over a rolling window

#### 📈 Visualizations Created
- Time-series plots for spread, mid price, and volatility
- Order book imbalance trends
- Rolling metrics visualizations using **Matplotlib**

---

## 🧠 Key Learnings

- Developed the ability to extract and clean real-time financial data
- Created market structure indicators from raw order book and trade data
- Visualized high-frequency indicators to understand short-term market behavior

# 📦 Week 3: Clustering & Visualization – Market Regime Detection

## 🎯 Goal
Apply **K-Means clustering** on engineered features to identify **distinct market regimes** and visualize them using **PCA**.

### 1️⃣ Data Cleaning & Resampling
- Converted timestamps to datetime format
- Resampled both datasets to **1-second intervals**
- Merged trade and order book data based on timestamp

**✅ Output:** `merged_df` (1-second granularity)

---

### 2️⃣ Feature Engineering
Engineered financial and market microstructure features including:

- **Statistical Features**:  
  - `price_var`, `value_per_second`, `avg_time_diff`
- **Volatility**:  
  - `log_return`, `volatility_10s`, `volatility_30s`
- **VWAP & VWAP Shifts**:  
  - `VWAP_10s`, `VWAP_30s`, `vwap_shift`
- **Order Book Imbalance**:  
  - `OBI_5`, `OBI_10`, `OBI_20`
- **Market Stats**:  
  - Buy/sell volume and price averages
- **Squared Returns**:  
  - `squared_log_return_var_10s`, `squared_log_return_var_30s`

**✅ Output:** `features_with_OBI_market.csv`

---

### 3️⃣ Clustering & Visualization

- Selected features and standardized with `StandardScaler`
- Chose optimal clusters (**k = 4**) using Elbow  methods
- Applied **KMeans Clustering**
- Reduced to 2D using **PCA** for visualization

**✅ Evaluation Metrics:**
- **Optimal k = 4**  

---

### 4️⃣ Cluster Interpretation

- Generated **cluster-wise feature averages** using heatmaps
- Interpreted market regimes based on volatility, imbalance, and price movement

| Cluster Type                 | Description                           |
|-----------------------------|---------------------------------------|
| Stable Bullish              | Low volatility, positive imbalance    |
| Stable Bearish              | Low volatility, negative imbalance    |
| High Volatility Bullish     | High volatility, positive price moves |
| Moderate Volatility Bearish | Medium volatility, falling prices     |

---

## 📈 Outcome

- Identified **4 unique market regimes** from raw HFT data
- Built a robust pipeline for **real-time market mood detection**
- Framework helps in **strategy design, risk management, and alpha generation**

---

