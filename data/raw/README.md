# Raw Data Documentation

## Overview
This contains raw datasets used to analyse the effect of international student enrolments on rental prices in New South Wales (NSW) and Victoria (VIC) from 2019 to 2024.


## Dataset 1: Rental Prices

**Source**: Australian Bureau of Statistics
**Accessed**: March 2026  
**Description**: Median weekly rent by state in Australia

**Variables used:**
* Date: Monthly observation  
* State: NSW and Victoria 
* Rental Price: Median weekly rent in AUD 

**Limitations:**
* Rental prices are reported as weekly values, which may not fully reflect total monthly rental costs  
* Does not capture within-state variation such as metropolitan and regional areas


## Dataset 2: International Student Enrolments

**Source**: Australian Government Department of Education  
**Accessed**: March 2026  
**Description**: International student enrolments by state  in Australia

**Variables used:**
* Date: Quarterly observation 
* State: NSW and Victoria  
* Enrolments: Number of international students enrolled

**Limitations:**
* YTD values represent cumulative enrolments and may not perfectly reflect the number of students actively residing in each period  
* Values increase within each year due to the cumulative nature of the data, which may influence trend interpretation  
* Despite this, enrolments serve as a reasonable proxy for student housing demand


## Dataset 3: Population

**Source**: Australian Bureau of Statistics
**Accessed**: March 2026
**Description**: Estimated resident population  

**Variables used:**
* Date: Quarterly  
* State: NSW and Victoria  
* Population: Total number of residents  

**Limitations:**
* Population includes all residents and does not specifically capture renters or housing demand groups  
 
* Does not explicitly distinguish between domestic residents and international students  


## Dataset 4: Housing Supply

**Source**: Australian Bureau of Statistics
**Accessed**: March 2026  
**Description**: Number of residential dwellings by state in Australia  

**Variables used:**
* Date: Quarterly  
* State: NSW and VIC
* Housing Supply: Total number of residential dwellings (in thousands)    

**Limitations:**
* Measures total dwellings and does not distinguish between occupied and vacant properties  
* Does not capture short-term changes in housing availability such as new construction.
* Does not account for differences in housing type or rental suitability   


## Dataset 5: Unemployment Rate

**Source**: Australian Bureau of Statistics
**Accessed**: March 2026  
**Description**: Unemployment rate by state in Australia  

**Variables used:**
* Date: Quarterly (constructed from monthly data)  
* State: NSW and VIC  
* Unemployment Rate: Seasonally adjusted unemployment rate (%)  

**Limitations:**
* Unemployment rate does not directly measure income levels or housing affordability  
* May not fully capture underemployment or labour market conditions   


## Dataset 6: Gross Domestic Product

**Source**: Australian Bureau of Statistics (ABS), accessed via Reserve Bank of Australia (RBA)  
**Accessed**: March 2026  
**Description**: Real Gross Domestic Product (chain volume measure) for Australia  

**Variables used:**
* Date: Quarterly  
* GDP: Real GDP (chain volume), in Australian dollars (million)  

**Limitations:**
* National-level data may not fully reflect economic conditions specific to New South Wales and Victoria  
* GDP is a broad measure of economic activity and does not directly capture housing market conditions
* May not capture short-term regional economic shocks affecting rental markets  
