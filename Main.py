import pandas as pd
from matplotlib import pyplot as plt
import numpy as np



df = pd.read_csv("Data/CPIAUCSL.csv")
unrate = pd.read_csv("Data/UNRATE.csv")
df["Inflation_Rate"] = df['CPIAUCSL'].pct_change(12) * 100
merged_df = pd.merge(df, unrate, on="observation_date", how='inner')
merged_df["observation_date"] = pd.to_datetime(merged_df["observation_date"])

def plot_phillips_curve(start, end):
    sub_df = merged_df[(merged_df['observation_date'] >= start) & (merged_df['observation_date'] <= end)]

    plt.figure()
    plt.scatter(sub_df["UNRATE"], sub_df["Inflation_Rate"], alpha=0.4)
    plt.title("Phillips Curve Visualization: " + str(start) + " to " + str(end))
    plt.ylabel("Inflation Rate")
    plt.xlabel("Unemployment Rate")
    m, b = np.polyfit(sub_df["UNRATE"], sub_df["Inflation_Rate"], 1)
    plt.plot(sub_df["UNRATE"], m*sub_df["UNRATE"] + b, color="orange", label="Regression Line")
    plt.grid(True)
    plt.legend()

def plot_graph():
    plt.figure()
    plt.plot(merged_df["observation_date"], merged_df["Inflation_Rate"], label="Inflation Rate")
    plt.plot(merged_df["observation_date"], merged_df["UNRATE"], label="Unemployment Rate")
    plt.title("Inflation and Employment from 1948-2025")
    plt.ylabel("Inflation and Unemployment Rate")
    plt.xlabel("Date")
    plt.legend()

plot_phillips_curve("1948-01-01", "1953-01-01")

plot_phillips_curve("1973-01-01", "1975-12-01")

plot_phillips_curve("1975-01-01", "1979-01-01")

plot_phillips_curve("1980-01-01", "1983-01-01")

plot_phillips_curve("1984-01-01", "1990-01-01")

plot_phillips_curve("2007-12-01", "2009-06-01")

plot_phillips_curve("2020-03-11", "2023-05-05")

plot_phillips_curve("2023-01-01", "2025-01-01")

plot_graph()

plt.show()
