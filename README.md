
# Cleared for Departure? Flight Delays and Cancellations in Texas

## Project Overview

This project analyzes flight delays, cancellations, and overall flight reliability across four major Texas airports. The goal is to identify patterns in flight delays and compare the reliability of different airports and airlines.

The project uses flight data from the U.S. Bureau of Transportation Statistics (BTS) Reporting Carrier On-Time Performance database.

## Team Information

- **Course:** INFO 450
- **Semester:** Fall 2026
- **Region:** Texas
- **Team:** Group Texas
- **Team Members:**
  - Nathnael Abraham
  - Andrea Ortiz
  - Nahom Ghiorghis
  - Danny Truong

## Airports Included

The analysis focuses on these four Texas airports:

- Dallas/Fort Worth International Airport (DFW)
- George Bush Intercontinental Airport (IAH)
- Austin-Bergstrom International Airport (AUS)
- San Antonio International Airport (SAT)

## Dataset

The dataset contains 60,000 sampled flight records covering August 2025 through July 2026.

Additional lookup files include:
- `carriers.csv`: Airline names and carrier types.
- `airports.csv`: Airport names, cities, and states.
- `Flight_Data_Dictionary.xlsx`: Descriptions of the dataset columns.

## Project Structure

```text
Texas-Flight-Analysis/
│
├── README.md
├── requirements.txt
├── project.ipynb
├── app.py
│
├── src/
│   ├── data_profile.py
│   ├── prepare_data.py
│   ├── airport_analysis.py
│   └── time_analysis.py
│
└── data/
    ├── flights_Texas.csv
    ├── carriers.csv
    ├── airports.csv
    └── flights_clean.csv
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone (https://github.com/truongdh3-vcu/info450-texas)
```

### 2. Open the project folder

```bash
cd info450-grouptexas
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook

```bash
jupyter notebook project.ipynb
```

### 5. Run the Streamlit Application

Once the application is completed, run:

```bash
streamlit run app.py
```

## Project Progress

The project follows the six phases of the CRISP-DM process:

- **Phase 1:** Business Understanding
- **Phase 2:** Data Understanding
- **Phase 3:** Data Preparation
- **Phase 4:** Exploratory Data Analysis
- **Phase 5:** Evaluation
- **Phase 6:** Deployment

For the In-Progress Review, Phases 1–3 are completed and Phase 4 is underway. The Streamlit application will be developed during Phase 6.

## Data Source

U.S. Bureau of Transportation Statistics (BTS)  
Reporting Carrier On-Time Performance Database

https://www.transtats.bts.gov/
