## Data Codebook

This codebook describes the variables included in the final dataset `master_dataset.csv`.  
All variables have been standardised to a **quarterly frequency** to ensure consistency across datasets.

| Variable Name | Description | Unit | Frequency | Source |
|--------------|------------|------|-----------|--------|
| Date | Time period of observation | Quarter | Quarterly | Derived |
| State | Australian state (New South Wales or Victoria) | Categorical | Quarterly | Derived |
| GDP ($ million) | Gross Domestic Product | AUD ($ million) | Quarterly | Reserve Bank of Australia (RBA) |
| Unemployment rate (%) | Percentage of labour force unemployed | Percentage (%) | Quarterly | Australian Bureau of Statistics (ABS) |
| Housing Supply | Number of residential dwellings | Thousands (000) | Quarterly | Australian Bureau of Statistics (ABS) |
| International Student Enrolments | Number of enrolled international students | Count | Quarterly | Australian Government Department of Education |
| Population | Total population | Count | Quarterly | Australian Bureau of Statistics (ABS) |
| Rental | Median weekly rent | AUD ($) | Quarterly | Australian Bureau of Statistics (ABS) |


### Notes

* Monthly variables (e.g., rental prices and unemployment rate) were converted to quarterly values using averaging.
* Quarterly variables (e.g., GDP, population, and housing supply) were used directly.
* All datasets were cleaned, standardised, and merged prior to analysis.