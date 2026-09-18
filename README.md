# Stock Market Dashboard

A desktop dashboard for visualizing stock price movements. Pick a stock, plot
its price over time, compare two stocks side by side, or pull up quick summary
statistics â€” all in a Tkinter window with live matplotlib charts.

![Python](https://img.shields.io/badge/Python-3.x-3776AB)
![pandas](https://img.shields.io/badge/pandas-data--analysis-150458)
![matplotlib](https://img.shields.io/badge/matplotlib-plots-11557c)
![GUI](https://img.shields.io/badge/GUI-Tkinter-blue)

## Features

- **Plot** any stock's price history as a line chart
- **Compare** two stocks on a single chart with a legend
- **Statistics** panel with average, min, max, standard deviation, and data points
- Stock dropdown populated automatically from the loaded CSV
- Clean layout: controls fixed on top, charts below

## Getting Started

### Requirements

Install the dependencies:

```bash
pip install pandas matplotlib
```

### Run the app

```bash
python Stock_Market_Dashboard/app.py
```

Select a stock from the dropdown, then choose **Plot Stock Data**, **Show
Statistics**, or **Compare Stocks**.

## Data

Price history is stored in `Stock_Market_Dashboard/stock_data.csv` with columns
`date, stock, price`. The included sample covers **AAPL, MSFT, GOOG, TSLA, AMZN**
for January 2025:

```
date,stock,price
2025-01-01,AAPL,145
2025-01-02,AAPL,150
...
```

To use your own data, keep the same columns and add rows with `YYYY-MM-DD` dates.

## Project structure

```
stock_market_dashboard_using_modules/
â””â”€â”€ Stock_Market_Dashboard/
    â”œâ”€â”€ app.py           # Tkinter + pandas + matplotlib dashboard
    â””â”€â”€ stock_data.csv   # Sample stock price data
```

## License

This project is open-source and available under the [MIT License](LICENSE).