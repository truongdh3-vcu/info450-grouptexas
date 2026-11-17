import pandas as pd
import numpy as np

def prepare_data():
    flights = pd.read_csv("data/flights_Texas.csv")
    carriers = pd.read_csv("data/carriers.csv")
    airports = pd.read_csv("data/airports.csv")
    original_rows = len(flights)
    duplicate_rows = int(flights.duplicated().sum())
    flights = flights.drop_duplicates().copy()
    rows_after_duplicates = len(flights)
    flights = flights.merge(carriers, left_on="Reporting_Airline", right_on="Code", how="left")
    flights = flights.drop(columns=["Code"])
    flights = flights.merge(airports, left_on="Dest", right_on="Code", how="left")
    flights = flights.drop(columns=["Code"])
    flights = flights.rename(columns={"Carrier": "AirlineName", "City": "DestinationCity", "State": "DestinationState"})
    flights["FlightDate"] = pd.to_datetime(flights["FlightDate"])
    flights["DepHour"] = (flights["CRSDepTime"] // 100).astype("Int64")
    flights["Weekend"] = flights["DayOfWeek"].isin([6, 7]).astype(int)
    flights["Route"] = flights["Origin"] + "-" + flights["Dest"]
    flights["DelayCategory"] = pd.cut(
        flights["ArrDelay"],
        bins=[-np.inf, 0, 15, 60, np.inf],
        labels=["Early", "On schedule", "Minor delay", "Major delay"],
        right=False
    )
    flights["DelayMinutes"] = flights["ArrDelay"].clip(lower=0)
    drop_columns = ["Year", "Quarter", "DayofMonth", "DOT_ID_Reporting_Airline", "OriginAirportID", "OriginStateFips", "DepTimeBlk", "Flights"]
    flights = flights.drop(columns=drop_columns)
    flights.to_csv("data/flights_clean.csv", index=False)
    print("Original rows:", original_rows)
    print("Duplicate rows removed:", duplicate_rows)
    print("Rows after duplicate removal:", rows_after_duplicates)
    print("Rows saved:", len(flights))
    print("Missing airline matches:", flights["AirlineName"].isna().sum())
    print("Missing destination matches:", flights["DestinationCity"].isna().sum())
    print("Completed flights:", len(flights[(flights["Cancelled"] == 0) & (flights["Diverted"] == 0)]))
    print("Cancelled flights:", int(flights["Cancelled"].sum()))
    print("Diverted flights:", int(flights["Diverted"].sum()))
    return flights
