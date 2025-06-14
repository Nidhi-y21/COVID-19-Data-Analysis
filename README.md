# COVID-19 Data Analysis

## Overview

This project analyzes global COVID-19 data to visualize pandemic trends such as confirmed cases, recoveries, and deaths. It uses mock data to simulate real-world reporting from multiple countries.

## Objective

To provide a visual story of COVID-19 growth, recovery trends, and death rates using line plots, area charts, and heatmaps.

## Dataset

* **Date**: Reporting date
* **Country**: Country name (e.g., USA, India, Brazil)
* **Confirmed**: Cumulative confirmed COVID-19 cases
* **Recovered**: Cumulative recovered cases
* **Deaths**: Cumulative deaths

## Process

1. **Data Generation**: Mock data created for 5 countries over 100 days
2. **Cleaning**: Parsing dates and casting numerical types
3. **Visualization**:

   * Line plot of confirmed cases
   * Area chart for death comparison
   * Heatmap of recovered cases by day and country

## Output Files

* `covid_data.csv`: Cleaned dataset
* `confirmed_line_plot.png`: Line plot of confirmed cases
* `deaths_area_chart.png`: Area chart comparing deaths
* `recovered_heatmap.png`: Heatmap of daily recoveries

## Requirements

* Python 3
* pandas, numpy, matplotlib, seaborn

## How to Run

```bash
pip install -r requirements.txt
python covid_data_analysis.py
```

## Conclusion

This analysis helps understand the spread and severity of COVID-19 across different countries and time periods, supporting public health decisions.
