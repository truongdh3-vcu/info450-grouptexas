import pandas as pd
import matplotlib.pyplot as plt

def monthly_trend(flights):
    completed = flights[(flights["Cancelled"] == 0) & (flights["Diverted"] == 0)].copy()
    completed["MonthPeriod"] = completed["FlightDate"].dt.to_period("M")
    monthly = completed.groupby("MonthPeriod").agg(
        Flights=("ArrDelay", "count"),
        OnTimeRate=("ArrDel15", lambda x: (x == 0).mean() * 100),
        MeanArrivalDelay=("ArrDelay", "mean")
    )
    print(monthly.round(2))
    monthly["OnTimeRate"].plot(kind="line", marker="o", title="Monthly On-Time Arrival Percentage", ylabel="On-time arrivals (%)", xlabel="Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return monthly

def daily_rolling_trend(flights):
    completed = flights[(flights["Cancelled"] == 0) & (flights["Diverted"] == 0)].copy()
    daily = completed.groupby("FlightDate").agg(
        OnTimeRate=("ArrDel15", lambda x: (x == 0).mean() * 100)
    )
    calendar = pd.date_range(daily.index.min(), daily.index.max(), freq="D")
    daily = daily.reindex(calendar)
    daily.index.name = "FlightDate"
    daily["Rolling7Day"] = daily["OnTimeRate"].rolling(7, min_periods=1).mean()
    daily[["OnTimeRate", "Rolling7Day"]].plot(title="Daily On-Time Rate with 7-Day Rolling Average", ylabel="On-time arrivals (%)", xlabel="Date", figsize=(12, 5))
    plt.tight_layout()
    plt.show()
    return daily
