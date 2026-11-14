import pandas as pd

def load_data():
    return pd.read_csv("data/flights_Texas.csv")

def profile_data(df):
    print("Rows and columns:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())
    print("Date range:", df["FlightDate"].min(), "to", df["FlightDate"].max())
    print("Data types:")
    print(df.dtypes)
    print("Value ranges:")
    print(df.describe(include="all").T)
    print("Missing values:")
    missing = df.isna().sum()
    missing = missing[missing > 0]
    missing_table = pd.DataFrame({
        "Missing": missing,
        "Percent": (missing / len(df) * 100).round(2)
    })
    print(missing_table)
    return missing_table

def missingness_evidence(df):
    groups = {
        "Tail_Number": ["Tail_Number"],
        "Departure fields": ["DepTime", "DepDelay", "DepDel15"],
        "TaxiOut": ["TaxiOut"],
        "Arrival time": ["ArrTime"],
        "Arrival delay and elapsed time": ["ArrDelay", "ArrDel15", "ActualElapsedTime"],
        "CancellationCode": ["CancellationCode"],
        "Distance": ["Distance"],
        "Delay causes": ["CarrierDelay", "WeatherDelay", "NASDelay", "SecurityDelay", "LateAircraftDelay"]
    }
    rows = []
    for label, columns in groups.items():
        count = int(df[columns[0]].isna().sum())
        rows.append({
            "Column group": label,
            "Columns": ", ".join(columns),
            "Missing rows": count,
            "Percent missing": round(count / len(df) * 100, 2)
        })
    return pd.DataFrame(rows)

def show_missingness_checks(df):
    for column in ["DepTime", "ArrDelay", "CancellationCode", "Distance", "CarrierDelay"]:
        print("\n", column)
        print(pd.crosstab(df[column].isna(), df["Cancelled"], margins=True))
        print(pd.crosstab(df[column].isna(), df["Diverted"], margins=True))
        if column == "CarrierDelay":
            print(pd.crosstab(df[column].isna(), df["ArrDel15"], margins=True))
