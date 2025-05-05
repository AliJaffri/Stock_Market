# 📊 Magnificent 7 Stock Viewer

An interactive Streamlit app to visualize historical closing prices of the Magnificent 7 stocks using a local CSV file.

## 🔧 Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Data Format

The `magnificent7.csv` file should be placed in the `data/` folder and structured like this:

| Date       | AAPL | MSFT | GOOGL | AMZN | NVDA | META | TSLA |
|------------|------|------|-------|------|------|------|------|
| 2023-01-02 | 125  | 230  | 90    | 95   | 145  | 200  | 110  |
