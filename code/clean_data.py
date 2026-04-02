# %% Gross Domestic Product (GDP)

"""

DESCRIPTION:
This script automates the cleaning and formatting of quarterly GDP data 
from the RBA. It handles row-level filtering, column-level filtering, 
column renaming, and standardizes date formats into a Year-Quarter string.

WHY:
Raw RBA files often contain metadata headers and inconsistent date 
indexing. This script creates a clean, chronological dataset restricted 
to 2019–2024 for comparative economic research.

"""

import pandas as pd
from pathlib import Path

def process_gdp_data(file_path):

    # --- STEP 1: DATA LOADING ---

    # Load raw RBA GDP CSV into a DataFrame
    df = pd.read_csv('../data/raw/rba_gdp_quarterly.csv')
    print("--- Step 1: Data Loaded ---")
    print(df.head(5))

    # --- STEP 2: DATA SELECTION & TRIMMING ---

    # Select only the first two columns (Date and GDP values)
    df = df.iloc[:, [0, 1]]

    # Remove non-data rows (metadata/headers) and reset the index for a clean start
    df = df.drop(index=[0, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reset_index(drop=True)

    # --- STEP 3: COLUMN STANDARDIZATION ---

    # Rename columns to provide clear, descriptive headers
    df.columns = ['Date', 'GDP ($ million)']

    # Remove any empty rows to maintain data integrity
    df = df.dropna()

    # --- STEP 4: DATE RE-FORMATTING ---

    # Convert 'Date' to a datetime object and drop any rows that fail conversion
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    # Transform date into a standardized 'YYYY-QX' string format
    df['Date'] = df['Date'].dt.year.astype(int).astype(str) + '-Q' + df['Date'].dt.quarter.astype(int).astype(str)

    # --- STEP 5: TIME-PERIOD FILTERING ---

    # Filter the dataset to keep only the specific research years (2019-2024)
    years_to_keep = ['2019', '2020', '2021', '2022', '2023', '2024']
    df = df[df['Date'].str[:4].isin(years_to_keep)]

    # --- STEP 6: CHRONOLOGICAL SORTING ---

    # Ensure the timeline flows correctly from the earliest to the latest quarter
    df = df.sort_values(by='Date', ascending=True)

    return df

if __name__ == "__main__":
   
   # Set paths for input and output locations
    input_file = '../data/raw/rba_gdp_quarterly.csv'
    output_folder = Path('../data/clean')
    output_file = output_folder / 'cleaned_gdp.csv'

    # Execute the processing function
    final_df = process_gdp_data(input_file)

    # --- STEP 7: EXPORTING CLEANED DATA ---

    # Save the final cleaned DataFrame to the target directory
    final_df.to_csv(output_file, index=False)

    print(f"--- Process Complete ---")
    print(f"File successfully saved to: {output_file}")
    print(final_df.head())

# %% Population

"""

DESCRIPTION:
This script cleans and transforms quarterly population data from the 
ABS. It extracts specific state-level data for New South Wales (NSW) 
and Victoria (VIC), standardizing the timeframe to 2019–2024.

WHY:
The dataset contain complex multi-index headers and data for all 
states. This script isolates the two largest economies (NSW and VIC) 
to allow for direct comparison with quarterly GDP trends.

"""

import pandas as pd
from pathlib import Path

def process_population_data(file_path):

    # --- STEP 1: DATA LOADING ---

    # Load the raw ABS population dataset
    df = pd.read_csv('../data/raw/abs_population_quarterly.csv')
    print("--- Step 1: Data Loaded ---")
    print(df.head(5))

    # --- STEP 2: FEATURE SELECTION ---

    # Select the specific columns for Date, and population for NSW and VIC
    df = df.iloc[:, [0, 19, 20]]

    # --- STEP 3: DATA TRIMMING ---

    # Remove metadata and reset the index
    df = df.drop(index=[1, 2, 3, 4, 5, 6, 7, 8, 9]).reset_index(drop=True)

    # --- STEP 4: COLUMN RENAMING ---

    # Assign clear, descriptive names to the selected columns
    df.columns = ['Date', 'Population NSW', 'Population VIC']

    # Remove any rows with missing values to ensure data quality
    df = df.dropna()

    # --- STEP 5: DATE STANDARDIZATION ---

    # Convert dates to datetime objects and handle any formatting errors
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    # Format dates into the 'YYYY-QX' string format
    df['Date'] = df['Date'].dt.year.astype(int).astype(str) + '-Q' + df['Date'].dt.quarter.astype(int).astype(str)

    # --- STEP 6: TIME-PERIOD FILTERING ---

    # Keep only the quarters within our 2019-2024 research window
    years_to_keep = ['2019', '2020', '2021', '2022', '2023', '2024']
    df = df[df['Date'].str[:4].isin(years_to_keep)]

    # --- STEP 7: CHRONOLOGICAL SORTING ---

    # Sort the data by date to ensure proper time-series flow
    df = df.sort_values(by='Date', ascending=True)

    return df

if __name__ == "__main__":
   
   # Set paths for input and output locations
    input_file = '../data/raw/abs_population_quarterly.csv'
    output_folder = Path('../data/clean')
    output_file = output_folder / 'cleaned_population.csv'

    # Execute the processing logic
    final_df = process_population_data(input_file)

    # --- STEP 8: EXPORTING CLEANED DATA ---

    # Save the processed data to the 'clean' folder without overwriting the raw source
    final_df.to_csv(output_file, index=False)

    print(f"--- Process Complete ---")
    print(f"File successfully saved to: {output_file}")
    print(final_df.head())

# %% Housing Supply

"""

DESCRIPTION:
This script cleans and transforms quarterly number of residential dwellings
data from the ABS. It extracts housing supply figures for NSW and VIC, 
standardizing the format to allow for correlation analysis with other factors.

WHY:
Housing supply is a lagging economic indicator. This script extracts 
specific state-level completions to help determine if supply met 
demand during the 2019–2024 period.

"""

import pandas as pd
from pathlib import Path

def process_housingsupply_data(file_path):

    # --- STEP 1: DATA LOADING ---
    
    # Load the raw ABS residential dwellings dataset
    df = pd.read_csv('../data/raw/abs_housingsupply_quarterly.csv')
    print("--- Step 1: Data Loaded ---")
    print(df.head(5))


    # --- STEP 2: FEATURE SELECTION ---

    # Select the specific columns for Date, and housing units for NSW and VIC
    df = df.iloc[:, [0, 37, 38]]

    # --- STEP 3: DATA TRIMMING ---

    # Remove metadata and reset the index
    df = df.drop(index=[1, 2, 3, 4, 5, 6, 7, 8, 9]).reset_index(drop=True)

    # --- STEP 4: COLUMN RENAMING ---

    # Rename columns to clearly state that units are measured in thousands
    df.columns = ['Date', 'Housing Supply NSW (thousands)', 'Housing Supply VIC (thousands)']

    # Remove any empty rows to ensure consistent data analysis
    df = df.dropna()

    # Convert to numeric and round to whole numbers
    df['Housing Supply NSW (thousands)'] = pd.to_numeric(df['Housing Supply NSW (thousands)'], errors='coerce').round(0)
    df['Housing Supply VIC (thousands)'] = pd.to_numeric(df['Housing Supply VIC (thousands)'], errors='coerce').round(0)

    # --- STEP 5: DATE STANDARDIZATION ---

    # Convert 'Date' column to datetime objects for accurate period extraction
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    # Reformat the date into the standardized 'YYYY-QX' string 
    df['Date'] = df['Date'].dt.year.astype(int).astype(str) + '-Q' + df['Date'].dt.quarter.astype(int).astype(str)

    # --- STEP 6: TIME-PERIOD FILTERING ---

    # Filter for the relevant research window: 2019-2024
    years_to_keep = ['2019', '2020', '2021', '2022', '2023', '2024']
    df = df[df['Date'].str[:4].isin(years_to_keep)]

    # --- STEP 7: CHRONOLOGICAL SORTING ---

    # Sort the data by date to maintain the time-series sequence
    df = df.sort_values(by='Date', ascending=True)

    return df

if __name__ == "__main__":
   
   # Define input and output locations
    input_file = '../data/raw/abs_housingsupply_quarterly.csv'
    output_folder = Path('../data/clean')
    output_file = output_folder / 'cleaned_housingsupply.csv'

    # Run the processing function
    final_df = process_housingsupply_data(input_file)

    # --- STEP 8: EXPORTING CLEANED DATA ---

    # Save the output to the 'clean' folder, ensuring the original raw file is untouched
    final_df.to_csv(output_file, index=False)

    print(f"--- Process Complete ---")
    print(f"File successfully saved to: {output_file}")
    print(final_df.head())

# %% Rental Price

"""

DESCRIPTION:
This script cleans monthly rental price data from the ABS. It performs 
a time-series resampling to convert monthly data points into quarterly 
averages, ensuring compatibility with our GDP and Population datasets.

WHY:
Rental data is often released monthly, but economic indicators like GDP 
are quarterly. This script standardizes the frequency and filters for 
the 2019–2024 period to analyze pandemic-era housing costs.

"""

import pandas as pd
from pathlib import Path

def process_rentalprice_data(file_path):

    # --- STEP 1: DATA LOADING ---

    # Load the raw monthly ABS rental price dataset
    df = pd.read_csv('../data/raw/abs_rentalprice_monthly.csv')
    print("--- Step 1: Data Loaded ---")
    print(df.head(5))

    # --- STEP 2: FEATURE SELECTION ---

    # Select the Date and the specific rental price columns for NSW and VIC
    df = df.iloc[:, [0, 1, 2]]

    # --- STEP 3: DATA TRIMMING ---

    # Remove the metadata header row and reset the index
    df = df.drop(index=[0]).reset_index(drop=True)

    # --- STEP 4: COLUMN STANDARDIZATION ---

    # Assign clear headers and convert 'Date' into a Python datetime format
    df.columns = ['Date', 'Rental NSW ($)', 'Rental VIC ($)']
    df['Date'] = pd.to_datetime(df['Date'], format='%b-%y', errors='coerce')

    # Drop any rows that failed date conversion and set Date as the index for resampling
    df = df.dropna(subset=['Date']).set_index('Date')

    # --- STEP 5: NUMERIC CONVERSION & RESAMPLING ---

    # Convert rental figures to numbers (handling errors) to allow for calculation
    df['Rental NSW ($)'] = pd.to_numeric(df['Rental NSW ($)'], errors='coerce')
    df['Rental VIC ($)'] = pd.to_numeric(df['Rental VIC ($)'], errors='coerce')

    # Convert monthly data to Quarterly Averages (QE = Quarter End) and round values
    df = df.resample('QE').mean().round().reset_index()

    # --- STEP 6: DATE RE-FORMATTING ---

    # Transform the date into the standardized 'YYYY-QX' string for cross-dataset merging
    df['Date'] = df['Date'].dt.year.astype(int).astype(str) + '-Q' + df['Date'].dt.quarter.astype(int).astype(str)

    # --- STEP 7: TIME-PERIOD FILTERING ---

    # Keep only the quarters within our 2019-2024 research window
    years_to_keep = ['2019', '2020', '2021', '2022', '2023', '2024']   
    df = df[df['Date'].str[:4].isin(years_to_keep)]

    # --- STEP 8: CHRONOLOGICAL SORTING ---

    # Sort the data by date to ensure the time-series sequence is correct
    df = df.sort_values(by='Date', ascending=True)

    return df

if __name__ == "__main__":
   
    # Set paths for input and output locations
    input_file = '../data/raw/abs_rentalprice_monthly.csv'
    output_folder = Path('../data/clean')
    output_file = output_folder / 'cleaned_rentalprice.csv'

    # Execute the processing function
    final_df = process_rentalprice_data(input_file)

    # --- STEP 9: EXPORTING CLEANED DATA ---

    # Save the quarterly averages to the 'clean' folder
    final_df.to_csv(output_file, index=False)

    print(f"--- Process Complete ---")
    print(f"File successfully saved to: {output_file}")
    print(final_df.head())

# %% Unemployment Rate

"""

DESCRIPTION:
This script cleans and transforms monthly unemployment rate data from 
the ABS. It calculates quarterly averages to align with macroeconomic 
indicators for the 2019–2024 period.

WHY:
Labor market dynamics shift monthly, but for a broad economic model, 
quarterly trends provide a clearer picture of structural changes, 
especially during the fluctuations of the early 2020s.

"""

import pandas as pd
from pathlib import Path

def process_unemploymentrate_data(file_path):

    # --- STEP 1: DATA LOADING ---

    # Load the raw monthly ABS unemployment rate dataset
    df = pd.read_csv('../data/raw/abs_unemploymentrate_monthly.csv')
    print("--- Step 1: Data Loaded ---")
    print(df.head(5))

    # --- STEP 2: FEATURE SELECTION ---

    # Isolate the Date and the primary Unemployment Rate (%) column
    df = df.iloc[:, [0, 2]]

    # --- STEP 3: DATA TRIMMING ---

    # Remove metadata and reset the index
    df = df.drop(index=[0]).reset_index(drop=True)

    # --- STEP 4: COLUMN STANDARDIZATION ---

    # Assign descriptive headers and convert the Date string into a datetime object
    df.columns = ['Date', 'Unemployment rate (%)']
    df['Date'] = pd.to_datetime(df['Date'], format='%b-%y', errors='coerce')

    # Remove rows with invalid dates and set the Date as the index for time-series math
    df = df.dropna(subset=['Date']).set_index('Date')

    # --- STEP 5: NUMERIC CONVERSION & RESAMPLING ---

    # Ensure the rate is treated as a number to allow for averaging
    df['Unemployment rate (%)'] = pd.to_numeric(df['Unemployment rate (%)'], errors='coerce')

    # Downsample from Monthly to Quarterly averages (QE) to match other datasets
    df = df.resample('QE').mean().round(1).reset_index()

    # --- STEP 6: DATE RE-FORMATTING ---

    # Standardize the date into the 'YYYY-QX' string format (e.g., 2024-Q1)
    df['Date'] = df['Date'].dt.year.astype(int).astype(str) + '-Q' + df['Date'].dt.quarter.astype(int).astype(str)

    # --- STEP 7: TIME-PERIOD FILTERING ---

    # Filter for the target research window: 2019-2024
    years_to_keep = ['2019', '2020', '2021', '2022', '2023', '2024']   
    df = df[df['Date'].str[:4].isin(years_to_keep)]

    # --- STEP 8: CHRONOLOGICAL SORTING ---

    # Sort the final dataset by time for logical analysis
    df = df.sort_values(by='Date', ascending=True)

    return df

if __name__ == "__main__":
   
    # Define file paths for the automated processing pipeline
    input_file = '../data/raw/abs_unemploymentrate_monthly.csv'
    output_folder = Path('../data/clean')
    output_file = output_folder / 'cleaned_unemploymentrate.csv'

    # Execute the processing function
    final_df = process_unemploymentrate_data(input_file)

    # --- STEP 9: EXPORTING CLEANED DATA ---

    # Save the quarterly results to the 'clean' folder
    final_df.to_csv(output_file, index=False)

    print(f"--- Process Complete ---")
    print(f"File successfully saved to: {output_file}")
    print(final_df.head())

# %% International Student Enrolments

"""

DESCRIPTION:
This script processes monthly international student enrolment data for NSW 
and Victoria. It filters for end-of-quarter snapshots (Mar, Jun, Sep, Dec) 
to align with quarterly rental price indices.

WHY:
International students represent a significant source of rental demand in 
inner-city Sydney and Melbourne. By isolating these enrolment figures 
against the 2019-2024 timeline, this script provides the 'Demand-Side' 
variable needed to test if student inflows correlate with the rental price 
surges observed in NSW and Victoria.

"""
import pandas as pd
from pathlib import Path

def process_internationalstudents_data(file_path):

    # --- STEP 1: DATA LOADING ---

    # Load the raw monthly ABS international student enrolment dataset
    df = pd.read_csv('../data/raw/abs_internationalstudent_monthly.csv')
    print("--- Step 1: Data Loaded ---")
    print(df.head(5))

    # --- STEP 2: FEATURE SELECTION ---

    # Isolate NSW and VIC enrolments to match our specific geographic research focus
    df = df.iloc[:, [0, 1, 2]]

    # --- STEP 3: COLUMN RENAMING ---

    # Standardize headers for clear identification in the final multi-variable model
    df.columns = ['Date', 'International Student Enrolments NSW', 'International Student Enrolments VIC']

    # --- STEP 4: DATE CONVERSION ---

    # Convert 'Date' to datetime to enable precise filtering of the academic calendar
    df['Date_dt'] = pd.to_datetime(df['Date'], format='%b-%y', errors='coerce')
    df = df.dropna(subset=['Date_dt'])

    # --- STEP 5: QUARTERLY SNAPSHOT FILTERING ---

    # Select Mar/Jun/Sep/Dec to match the frequency of Rental Price Index reporting
    df = df[df['Date_dt'].dt.month.isin([3, 6, 9, 12])]

    # --- STEP 6: STANDARDIZED DATE FORMATTING ---

    # Format as 'YYYY-QX' to allow seamless merging with Rental and GDP datasets
    df['Date'] = ( 
        df['Date_dt'].dt.year.astype(str) + '-Q' + df['Date_dt'].dt.quarter.astype(str)
    )

    # --- STEP 7: RESEARCH TIMEFRAME FILTERING ---

    # Focus on 2019-2024 to capture the 'Pre-Pandemic', 'Lockdown', and 'Recovery' phases
    years_to_keep = ['2019', '2020', '2021', '2022', '2023', '2024']
    df = df[df['Date'].str[:4].isin(years_to_keep)]
   
   # --- STEP 8: FINAL CLEANUP & SORTING ---

    # Drop temporary helpers and ensure chronological order for time-series analysis
    df = df.drop(columns=['Date_dt'])
    df = df.sort_values(by='Date', ascending=True).reset_index(drop=True)

    return df

if __name__ == "__main__":
   
    # Define file paths for the automated processing pipeline
    input_file = '../data/raw/abs_internationalstudent_monthly.csv'
    output_folder = Path('../data/clean')
    output_file = output_folder / 'cleaned_internationalstudent.csv'

    # Execute the processing function
    final_df = process_internationalstudents_data(input_file)

    # --- STEP 9: EXPORTING CLEANED DATA ---

    # Save output to 'clean' folder
    final_df.to_csv(output_file, index=False)

    print(f"--- Process Complete ---")
    print(f"File successfully saved to: {output_file}")
    print(final_df.head())
    
# %% Merge Datasets into One Master Dataset

"""

DESCRIPTION:
This script integrates six distinct economic datasets (GDP, Population, Housing, 
Rent, Unemployment, and International Students) into a unified Master Dataset. 
It performs a multi-way join and reshapes the data from a 'Wide' format to 
a 'Long/Panel' format, organized by Date and State.

WHY:
To test the impact of international students on rental prices, we need all 
variables in a single observation row. This script aligns 'Demand' 
(Students/Population), 'Supply' (Housing), and 'Price' (Rent), while 
controlling for broader 'Economic Health' (GDP/Unemployment), allowing 
for a direct comparison between NSW and Victoria from 2019–2024.

"""
import pandas as pd
from functools import reduce

# --- STEP 1: DEFINE DATA SOURCES ---

# List all cleaned CSV files prepared in previous processing steps
file_paths = [
    '../data/clean/cleaned_gdp.csv', 
    '../data/clean/cleaned_population.csv', 
    '../data/clean/cleaned_housingsupply.csv', 
    '../data/clean/cleaned_rentalprice.csv', 
    '../data/clean/cleaned_unemploymentrate.csv', 
    '../data/clean/cleaned_internationalstudent.csv'
    ]

# --- STEP 2: BULK LOADING ---

# Read all cleaned datasets into a list of DataFrames
dfs = [pd.read_csv(fp) for fp in file_paths]

# --- STEP 3: MULTI-DATASET MERGING ---

# Use 'reduce' to merge all 6 DataFrames on the 'Date' column in one pass
# This ensures every row represents a unique Year-Quarter (e.g., 2022-Q1)
df_merged = reduce(lambda left, right: pd.merge(left, right, on=left.columns[0]), dfs)

# --- STEP 4: DATA RESTRUCTURING (MELTING) ---

# Transition from 'Wide' format (columns for every state) to 'Long' format
# We keep national-level indicators (GDP/Unemployment) as fixed variables
df_long = df_merged.melt(id_vars=['Date', 'GDP ($ million)', 'Unemployment rate (%)'],
                         var_name='Old_Col', value_name='Value')

# --- STEP 5: GEOGRAPHIC ATTRIBUTION ---

# Extract 'State' (NSW/VIC) and 'Metric' name from the merged column titles
# This allows us to compare the two states side-by-side in our analysis
df_long[['Metric', 'State']] = df_long['Old_Col'].str.extract(r'(.*?)\s*(NSW|VIC)')

# --- STEP 6: FINAL PIVOTING ---

# Pivot the table so each row represents a unique Date + State combination
# Result: One row for NSW 2022-Q1, one row for VIC 2022-Q1, etc.
df_final = df_long.pivot_table(index=['Date', 'State', 'GDP ($ million)', 'Unemployment rate (%)'], 
                               columns='Metric', 
                               values='Value').reset_index()

# --- STEP 7: MASTER EXPORT ---

# Save the final research-ready dataset
df_final.to_csv('../data/clean/master_dataset.csv', index=False)


