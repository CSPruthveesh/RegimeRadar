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



> This README summarizes progress up to Week 2. The upcoming weeks will focus on applying machine learning techniques for pattern discovery in market microstructure data.
