# ecc3479-project

## Research Question
What is the effect of international student enrolments on rental prices in New South Wales and Victoria from 2019 to 2024?

## Data Sources
1. Australian Bureau of Statistics (ABS)
   * Median weekly rent
   * Housing supply
   * Unemployment rate
   * Population

2. Australian Government Department of Education
   * International student enrolments

3. Reserve Bank of Australia (RBA)
   * Gross domestic product


## Repository Structure

* `code/` 
 Contains the main data processing script `clean_data.py` used to clean, transform, and merge all raw datasets.

* `data/raw/` 
 Stores original, unprocessed datasets obtained from external sources.

* `data/clean/` 
 Stores cleaned and processed datasets, including intermediate files and the final `master_dataset.csv`.

* `docs/` 
 Contains project documentation, including research notes and methodological explanations.
 * `outputs/` 
 Stores final outputs such as visualisations, summary tables, and analysis results.

* `requirements.txt` 
 Lists all Python packages required to reproduce the project environment.

## How to Run from Scratch

Follow these steps to reproduce the `master_dataset.csv` on your local device:

### 1. Prerequisites
Ensure you have **Python 3.9+** installed. Check this by running the following command in your terminal:
```
python3 --version
```

### 2. Clone the Repository
Download or clone this repository to your local directory:
```
git clone https://github.com/aliffhmzah/ecc3479-project.git
cd ecc3479-project
```

### 3. Set Up the Environment
Install the required libraries by running the following command in your terminal:
```
python3 -m pip install -r requirements.txt
```

### 4. Execute the Data Pipeline
Run the main cleaning and merging script from the root directory:
```
python3 code/clean_data.py
```
All required raw datasets must be placed in `data/raw/`.
Once the process is complete, navigate to the `data/clean/` folder. You should see the following new files generated:

  * `cleaned_gdp.csv`
  * `cleaned_population.csv`
  * `cleaned_housingsupply.csv`
  * `cleaned_rentalprice.csv`
  * `cleaned_unemploymentrate.csv`
  * `cleaned_internationalstudent.csv`
  * `master_dataset.csv`


## Manual Steps Outside the Code

While the data cleaning and merging are fully automated, the following manual steps were required to establish the project environment:

### 1. Data Sourcing & Acquisition

* **Sourcing:** Raw data was manually downloaded in `.xlsx` (Excel) format from the **Australian Bureau of Statistics (ABS)**, the **Reserve Bank of Australia (RBA)** and the **Australian Government Department of Education**.

* **Format Conversion:** Each Excel workbook was manually reviewed and exported as a `.csv` file to ensure compatibility with the Python `pandas` engine.

### 2. Complex Extraction (International Students)

* **Pivot Table Extraction:** The International Student Enrolment dataset was originally provided by the Australian Government Department of Education in a pivot table format with multiple hierarchical dimensions.
* **Manual Filtering:** To prepare this for the Python pipeline, filters were manually applied in Excel to isolate the states and months data points.
* **Clean Export:** These filtered results were then converted into a standardized flat-file CSV format before being processed by the Python pipeline.

### 3. File Standardization
To ensure the `code/clean_data.py` script functions correctly, the converted CSV files were moved into the `data/raw/` directory and renamed consistently to the following:

* `rba_gdp_quarterly.csv`
* `abs_population_quarterly.csv`
* `abs_residentialbuilding_quarterly.csv`
* `abs_rentalprice_monthly.csv`
* `abs_unemploymentrate_monthly.csv`
* `abs_internationalstudent_monthly.csv`

### 4. Documentation & Codebook
A manual review of the raw metadata was performed to identify and document:

* **Units:** Distinguishing between absolute figures (Population) and scaled figures (GDP in $ Millions).
* **Frequencies:** Identifying which datasets required monthly-to-quarterly resampling (Rent and Unemployment) versus those already in quarterly format.

## Order Scripts are Run

The data processing pipeline is executed using a single script: `code/clean_data.py`

No additional scripts are required, as the entire pipeline is contained within this file.

Within this script, the workflow is executed sequentially in the following stages:

* Each dataset is cleaned and processed independently.
* Datasets are standardised and transformed where required.
* All datasets are merged into a single dataset.
* The merged dataset is reshaped into long format.
* Cleaned files and the final dataset are saved to `data/clean/`.

The script is designed to run from start to finish without manual intervention.

This pipeline ensures that all datasets are processed consistently and reproducibly, supporting reliable empirical analysis.

## Exploratory Data Analysis

### Overview of the Dataset

The dataset captures the relationship between rental prices and key economic and demographic factors in New South Wales (NSW) and Victoria (VIC) over time (2019–2024).

* Rental prices (median weekly rent)
* International student enrolments
* Housing supply (number of dwellings)
* Population
* Unemployment rate
* Gross Domestic Product (GDP)

Overall, the dataset is structured as a state-level time series (panel dataset), allowing comparison across both time and regions.

### Initial Variable Selection and Focus

Initial exploration focused on:

* Rental prices (main outcome variable)
* International student enrolments (key explanatory variable)

These were prioritised because they directly relate to the research question. Additional variables such as housing supply, population, unemployment rate, and GDP were then examined as potential control variables to account for broader economic conditions.

### Distributional Characteristics of the Data

Several key patterns emerged from summary statistics and skewness:

* Rental prices showed positive skewness, indicating a concentration of observations at lower values with a tail toward higher rents.
* Unemployment rate also displayed positive skewness, suggesting occasional spikes during certain periods.
* Housing supply and population appeared approximately symmetrical, reflecting relatively stable growth over time.
* International student enrolments showed mild skewness, likely influenced by structural changes.

### Insights from Scatter Plots and Correlation Analysis

Scatter plots and correlation analysis revealed:

* A positive association between international student enrolments and rental prices, suggesting that higher student presence may be linked to increased housing demand.
* A weak or mixed relationship between housing supply and rental prices, which may reflect supply constraints, lag effects, or geographic mismatches.
* Population and rental prices showed a generally positive relationship, consistent with demand-side economic theory.
* Some variables exhibited moderate correlations, but not at levels indicating severe multicollinearity.

However, these relationships are associational rather than causal, and may be influenced by omitted variables or underlying time trends.

