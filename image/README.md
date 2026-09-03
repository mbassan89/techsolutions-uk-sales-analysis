# TechSolutions UK Sales Analysis

## Project Overview

This project analyses sales data for a fictional UK technology retailer using Python and Pandas.

I created this project independently as a portfolio exercise to demonstrate my practical skills in Python and Pandas, including cleaning, transforming and querying structured data to answer business questions.

The project follows a complete data analysis workflow, from data quality checking and cleaning to data preparation, analysis, visualisation and business insights.

## Project Objectives

- Clean and prepare sales and product data for analysis.
- Combine multiple datasets into a single analysis-ready dataset.
- Calculate key sales metrics.
- Analyse performance across products, regions, customer types and salespeople.
- Create visualisations and identify useful business insights.

## Dataset

The project uses two synthetic CSV datasets created specifically for this exercise:

- `sale_data.csv` - sales transactions including order date, product, quantity, region, customer type, salesperson, payment method and discount.
- `product.csv` - product information including category and unit price.

Data quality issues were intentionally included to simulate a realistic data cleaning process.

## Data Quality and Cleaning

Initial checks identified missing values, duplicate rows, inconsistent categorical values, invalid quantities, discounts, dates and prices, as well as inconsistent product names between the two datasets.

The data was cleaned and standardised using Pandas methods including:

- `fillna()`
- `drop_duplicates()`
- `replace()`
- `str.strip()`
- `loc[]`
- `mask()`
- `to_datetime()`

The cleaning process also included validation checks to confirm that no missing values, duplicate rows, invalid numeric values or unmatched products remained.

### Cleaning Assumption

The missing `UnitPrice` for `Keyboard` could not be recovered from another record in the available data. A value of £70 was therefore assigned as a reasonable estimate after reviewing comparable products in the `Accessories` category.

In a real-world analysis, missing or invalid values would ideally be verified against the original source system or another reliable business source rather than estimated.

