# Exploratory Data Analysis of Global Life Expectancy and Healthy Life Expectancy

## Project Overview

This project performs Exploratory Data Analysis (EDA) of global life expectancy and healthy life expectancy data from **2000 to 2021**.

The analysis examines changes across countries, differences between males and females, the gap between life expectancy and healthy life expectancy, variations across WHO geographic regions, and the relationship between life expectancy and healthy life expectancy.

---

## Project Information

| Item | Details |
|---|---|
| **Project Title** | Exploratory Data Analysis of Global Life Expectancy and Healthy Life Expectancy |
| **Industry Name** | Global Health |
| **Dataset Name** | Global Life Expectancy and Healthy Life Expectancy data (2000–2021) |
| **Dataset Source** | Not specified in the provided project information |
| **Analysis Period** | 2000–2021 |

---

## Problem Statement

Life expectancy and healthy life expectancy vary considerably across countries, genders, and geographic regions. Understanding these variations can help identify important patterns in global health and differences in the number of years people are expected to live in good health.

This project aims to explore global life expectancy and healthy life expectancy data from 2000 to 2021 to identify trends and relationships across countries. The analysis focuses on factors such as life expectancy, healthy life expectancy, gender differences, the gap between life expectancy and healthy life expectancy, and variations across WHO geographic regions.

The findings from this exploratory analysis can provide useful insights into global health patterns, differences in longevity and healthy years of life, and the variations between countries and regions.

---

## Proposed Solution / Analysis Questions

Python-based Exploratory Data Analysis is used to clean, transform, analyze, and visualize the life expectancy and healthy life expectancy datasets.

The project addresses the following questions:

1. How has life expectancy changed across countries from 2000 to 2021?
2. How has healthy life expectancy changed across countries from 2000 to 2021?
3. Which countries had the highest and lowest life expectancy in the latest available year?
4. Which countries had the highest and lowest healthy life expectancy in the latest available year?
5. How does life expectancy differ between males and females across countries?
6. How does healthy life expectancy differ between males and females across countries?
7. What is the gap between life expectancy and healthy life expectancy across countries?
8. Which countries have the largest and smallest gap between life expectancy and healthy life expectancy?
9. How does life expectancy vary across different geographic regions?
10. What is the relationship between life expectancy and healthy life expectancy across countries?

---

## Tools & Technologies

- **Python**
- **Jupyter Notebook**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## Project Workflow

**Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations**

### Workflow Description

- **Industry Selection:** Global Health
- **Problem Identification:** Analyze variations and patterns in life expectancy and healthy life expectancy.
- **Dataset Collection:** Life expectancy and healthy life expectancy datasets covering 2000–2021.
- **Data Cleaning:** Standardized column names, checked data types, duplicates, missing values, geographic information, and analysis columns.
- **Data Transformation:** Merged the life expectancy and healthy life expectancy data and calculated the health gap.
- **Data Analysis:** Performed trend, country-level, gender, gap, regional, distribution, and relationship analysis.
- **Data Visualization:** Created charts for the analyses performed.
- **Insights:** Identified changes, country differences, gender gaps, regional differences, health gaps, and the relationship between the two measures.
- **Recommendations:** Recommendations are based on the observed patterns in the analyzed data.

---

## Data Analysis & Visualization

The project includes the following analyses and visualizations:

### 1. Trend Analysis

- Average life expectancy across countries from 2000 to 2021.
- Average healthy life expectancy across countries from 2000 to 2021.
- Country-level changes between 2000 and 2021.

### 2. Country Comparison Analysis

- Highest and lowest life expectancy by country in 2021.
- Highest and lowest healthy life expectancy by country in 2021.
- Countries with the largest and smallest life expectancy–healthy life expectancy gaps in 2021.

### 3. Gender Analysis

- Comparison of male and female life expectancy in 2021.
- Female–male life expectancy gap.
- Comparison of male and female healthy life expectancy in 2021.
- Female–male healthy life expectancy gap.

### 4. Distribution Analysis

- Distribution of the life expectancy–healthy life expectancy gap in 2021.

### 5. Regional Analysis

- Life expectancy across WHO regions in 2021.

### 6. Relationship and Correlation Analysis

- Relationship between life expectancy and healthy life expectancy across countries in 2021.
- Correlation between life expectancy and healthy life expectancy.

---

## Key Insights

The following insights are obtained directly from the analysis:

- Average life expectancy increased from **66.92 years in 2000** to **71.23 years in 2021**.
- Average healthy life expectancy increased from **58.30 years in 2000** to **61.84 years in 2021**.
- Among the countries analyzed in 2021, **Japan** had the highest life expectancy at approximately **84.46 years**, while **Lesotho** had the lowest at approximately **51.48 years**.
- **Singapore** had the highest healthy life expectancy in 2021 at approximately **73.65 years**, while **Lesotho** had the lowest at approximately **44.63 years**.
- Average female life expectancy in 2021 was approximately **73.69 years**, compared with **68.85 years** for males.
- The average female–male life expectancy gap was approximately **4.84 years**.
- Average female healthy life expectancy in 2021 was approximately **62.87 years**, compared with **60.83 years** for males.
- The average female–male healthy life expectancy gap was approximately **2.04 years**.
- The average gap between life expectancy and healthy life expectancy in 2021 was approximately **9.39 years**.
- **Australia** had the largest life expectancy–healthy life expectancy gap in 2021 at approximately **12.50 years**.
- **Somalia** had the smallest gap at approximately **6.53 years**.
- Among the WHO regions analyzed in 2021, **Western Pacific** had the highest average life expectancy at approximately **77.42 years**, while **Africa** had the lowest at approximately **63.55 years**.
- The correlation between life expectancy and healthy life expectancy across countries in 2021 was approximately **0.9952**, indicating a very strong positive relationship in the analyzed data.

---

## Recommendations

Based only on the findings from this analysis:

- Pay particular attention to countries with lower life expectancy and healthy life expectancy when examining differences in global health outcomes.
- Further examine the countries showing larger differences between life expectancy and healthy life expectancy to understand the observed health gap.
- Consider the observed female–male differences when analyzing life expectancy and healthy life expectancy across countries.
- Compare regional patterns to better understand the differences in life expectancy across WHO geographic regions.
- Use the strong relationship between life expectancy and healthy life expectancy as a basis for further analysis of healthy years of life across countries.

---

## Visualization Screenshots

### Average Life Expectancy Across Countries (2000-2021)

![Average Life Expectancy Across Countries](Visualizations/Average%20Life%20Expectancy%20Across%20Countries%20%282000-2021%29.png)

### Average Healthy Life Expectancy Across Countries (2000-2021)

![Average Healthy Life Expectancy Across Countries](Visualizations/Average%20Healthy%20Life%20Expectancy%20Across%20Countries%20%282000-2021%29.png)

### Highest and Lowest Life Expectancy by Country (2021)

![Highest and Lowest Life Expectancy by Country](Visualizations/Highest%20and%20Lowest%20Life%20Expectancy%20by%20Country%20%282021%29.png)

### Highest and Lowest Healthy Life Expectancy by Country (2021)

![Highest and Lowest Healthy Life Expectancy by Country](Visualizations/Highest%20and%20Lowest%20Healthy%20Life%20Expectancy%20by%20Country%20%282021%29.png)

### Average Life Expectancy by Sex (2021)

![Average Life Expectancy by Sex](Visualizations/Average%20Life%20Expectancy%20by%20Sex%20%282021%29.png)

### Average Healthy Life Expectancy by Sex (2021)

![Average Healthy Life Expectancy by Sex](Visualizations/Average%20Healthy%20Life%20Expectancy%20by%20Sex%20%282021%29.png)

### Distribution of Life Expectancy-Healthy Life Expectancy Gap (2021)

![Distribution of Life Expectancy-Healthy Life Expectancy Gap](Visualizations/Distribution%20of%20Life%20Expectancy-Healthy%20Life%20Expectancy%20Gap%20%282021%29.png)

### Countries with the Largest and Smallest Health Gap (2021)

![Countries with the Largest and Smallest Health Gap](Visualizations/Countries%20with%20the%20Largest%20and%20Smallest%20Health%20Gap%20%282021%29.png)

### Life Expectancy Across WHO Regions (2021)

![Life Expectancy Across WHO Regions](Visualizations/Life%20Expectancy%20Across%20WHO%20Regions%20%282021%29.png)

### Relationship Between Life Expectancy and Healthy Life Expectancy (2021)

![Relationship Between Life Expectancy and Healthy Life Expectancy](Visualizations/Relationship%20Between%20Life%20Expectancy%20and%20Healthy%20Life%20Expectancy%20%282021%29.png)

---

## Project Structure

```text
Data-Analysis-Python-Project/
│
├── README.md
│
├── Dataset/
│   ├── raw_dataset.csv
│   └── cleaned_dataset.csv
│
├── Notebook/
│   └── Data_Analysis_EDA.ipynb
│
├── Python/
│   ├── data_loading.ipynb
│   ├── data_cleaning.ipynb
│   ├── exploratory_analysis.ipynb
│   └── data_visualization.ipynb
│
├── Visualizations/
│   ├── Average Life Expectancy Across Countries (2000-2021).png
│   ├── Average Healthy Life Expectancy Across Countries (2000-2021).png
│   ├── Highest and Lowest Life Expectancy by Country (2021).png
│   ├── Highest and Lowest Healthy Life Expectancy by Country (2021).png
│   ├── Average Life Expectancy by Sex (2021).png
│   ├── Average Healthy Life Expectancy by Sex (2021).png
│   ├── Distribution of Life Expectancy-Healthy Life Expectancy Gap (2021).png
│   ├── Countries with the Largest and Smallest Health Gap (2021).png
│   ├── Life Expectancy Across WHO Regions (2021).png
│   └── Relationship Between Life Expectancy and Healthy Life Expectancy (2021).png
│
└── Documentation/
    └── Project_Report.pdf
```

---

## Author

- **Name:** Hariharan
- **Student ID:** AF05311607
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** [ANP-D7444]
