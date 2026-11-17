import pandas as pd
import matplotlib.pyplot as plt

def airport_reliability(flights):
    completed = flights[(flights["Cancelled"] == 0) & (flights["Diverted"] == 0)].copy()
    scheduled = flights.groupby("Origin").agg(
        Scheduled=("Origin", "size"),
        Cancelled=("Cancelled", "sum"),
        Diverted=("Diverted", "sum")
    )
    scheduled["CancellationRate"] = scheduled["Cancelled"] / scheduled["Scheduled"] * 100
    scheduled["DiversionRate"] = scheduled["Diverted"] / scheduled["Scheduled"] * 100
    completed_stats = completed.groupby("Origin").agg(
        Completed=("ArrDelay", "count"),
        OnTimeRate=("ArrDel15", lambda x: (x == 0).mean() * 100),
        MeanArrivalDelay=("ArrDelay", "mean")
    )
    result = scheduled.join(completed_stats).round(2)
    print(result)
    return result

def arrival_delay_summary(flights):
    completed = flights[(flights["Cancelled"] == 0) & (flights["Diverted"] == 0)]
    print(completed["ArrDelay"].describe())
    print("Skewness:", completed["ArrDelay"].skew())
    print("Kurtosis:", completed["ArrDelay"].kurt())
    print("On-time arrival percentage:", round((completed["ArrDel15"] == 0).mean() * 100, 2))
    print("Cancellation rate:", round(flights["Cancelled"].mean() * 100, 2))
    print("Diversion rate:", round(flights["Diverted"].mean() * 100, 2))

def airport_charts(result, flights):
    result["OnTimeRate"].plot(kind="bar", title="On-Time Arrival Percentage by Texas Airport", ylabel="On-time arrivals (%)", xlabel="Origin airport")
    plt.tight_layout()
    plt.show()
    completed = flights[(flights["Cancelled"] == 0) & (flights["Diverted"] == 0)]
    completed["ArrDelay"].plot(kind="hist", bins=50, title="Distribution of Arrival Delays", xlabel="Arrival delay (minutes)", ylabel="Number of flights")
    plt.tight_layout()
    plt.show()
