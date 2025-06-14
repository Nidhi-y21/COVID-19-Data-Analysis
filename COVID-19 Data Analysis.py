# COVID-19 Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate mock COVID-19 data
np.random.seed(42)
dates = pd.date_range(start="2020-01-01", periods=100)
countries = ['USA', 'India', 'Brazil', 'Russia', 'UK']
data = []
for country in countries:
    confirmed = np.cumsum(np.random.randint(100, 1000, size=len(dates)))
    recovered = confirmed * np.random.uniform(0.6, 0.9, size=len(dates))
    deaths = confirmed * np.random.uniform(0.01, 0.05, size=len(dates))
    for i in range(len(dates)):
        data.append([dates[i], country, confirmed[i], recovered[i], deaths[i]])

covid_df = pd.DataFrame(data, columns=['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths'])

# Save dataset
covid_df.to_csv("covid_data.csv", index=False)

# 2. Data Cleaning
covid_df['Date'] = pd.to_datetime(covid_df['Date'])
covid_df[['Confirmed', 'Recovered', 'Deaths']] = covid_df[['Confirmed', 'Recovered', 'Deaths']].astype(int)

# 3. Line Plot - Cumulative Confirmed Cases
plt.figure(figsize=(12, 6))
for country in countries:
    subset = covid_df[covid_df['Country'] == country]
    plt.plot(subset['Date'], subset['Confirmed'], label=country)
plt.title("Cumulative Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.legend()
plt.tight_layout()
plt.savefig("confirmed_line_plot.png")
plt.show()

# 4. Area Chart - Deaths Comparison
pivot_deaths = covid_df.pivot(index='Date', columns='Country', values='Deaths')
pivot_deaths.plot.area(figsize=(12, 6), title="COVID-19 Deaths Comparison (Area Chart)")
plt.ylabel("Deaths")
plt.tight_layout()
plt.savefig("deaths_area_chart.png")
plt.show()

# 5. Heatmap - Daily Recovered Cases
heatmap_data = covid_df.pivot_table(index='Country', columns='Date', values='Recovered')
plt.figure(figsize=(14, 5))
sns.heatmap(heatmap_data, cmap='YlGnBu')
plt.title("Daily Recovered Cases Heatmap")
plt.tight_layout()
plt.savefig("recovered_heatmap.png")
plt.show()

print("\nCOVID-19 Data Analysis complete. Dataset saved as 'covid_data.csv'.")
print("Plots saved: 'confirmed_line_plot.png', 'deaths_area_chart.png', 'recovered_heatmap.png'.")
