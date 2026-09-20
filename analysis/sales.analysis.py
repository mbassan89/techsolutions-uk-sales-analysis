# TechSolutions UK Sales Analysis
import pandas as pd

# Load datasets
sales = pd.read_csv("data/sale_data.csv")
products = pd.read_csv("data/product.csv")

# Inspect the data
print(sales.head())
print(products.head())

# Check dataset sizes
print(sales.shape)
print(products.shape)

# Check dataset structure and data types
sales.info()
products.info()


# SALES DATA CHECKING
print("\n=== SALES DATA CHECKING ===")

# Check descriptive statistics
print(sales.describe())

# Check for missing values
print(sales.isna().sum())

# Check for duplicate rows
print(sales.duplicated().sum())
print(sales[sales.duplicated()])

# Check unique values in categorical columns
print(sales["Region"].unique())
print(sales["Customer Type"].unique())
print(sales["Sales Person"].unique())
print(sales["PaymentMethod"].unique())
print(sales["Product"].unique())

# Check numeric values are within valid ranges
print(sales[sales["Quantity"] <= 0])
print(sales[(sales["Discount"] < 0) | (sales["Discount"] > 100)])

# Check for invalid dates
print(sales
      [pd.to_datetime(
        arg= sales["OrderDate"],
        errors="coerce", 
        format="%d/%m/%Y"
      ).isna()
])

# Check that all products in sales exist in the products dataset
print(sales[~sales["Product"].isin(products["Product"])])



# PRODUCTS DATA CHECKING
print("\n=== PRODUCTS DATA CHECKING ===")

# Check descriptive statistics
print(products.describe())

# Check for missing values
print(products.isna().sum())

# Check for duplicate rows
print(products.duplicated().sum())
print(products[products.duplicated()])

# Check unique values in categorical columns
print(products["Category"].unique())

# Check numeric values are within valid ranges
print(products[products["UnitPrice"] <= 0])

# Check CostPrice values are valid
print(products[products["CostPrice"] <= 0])

# Check that all ProductIDs in sales exist in the products dataset
print(
    sales[
        ~sales["ProductID"].isin(products["ProductID"])
    ]
)



# SALES DATA CLEANING
print("\n=== SALES DATA CLEANING ===")

# Fill missing Region values with "Unknown"
sales["Region"] = sales["Region"].fillna("Unknown")

# Verify missing Region values
print(sales["Region"].isna().sum())

# Fill missing PaymentMethod values with "Not Recorded"
sales["PaymentMethod"] = sales[
    "PaymentMethod"].fillna("Not Recorded"
)

# Verify missing PaymentMethod values
print(sales["PaymentMethod"].isna().sum())

# Remove duplicate rows
sales.drop_duplicates(inplace=True)

# Verify duplicate rows were removed
print(sales.duplicated().sum())

# Standardise Region values
sales["Region"] = sales["Region"].replace(
    to_replace="NorthWest",
    value="North West"
)

# Verify Region values
print(sales["Region"].unique())

# Standardise Customer Type values
sales["Customer Type"] = sales["Customer Type"].replace(
    to_replace="consumer",
    value="Consumer"
)

# Verify Customer Type values
print(sales["Customer Type"].unique())

# Remove leading and trailing spaces from Sales Person values
sales["Sales Person"] = sales["Sales Person"].str.strip()

# Verify Sales Person  values
print(sales["Sales Person"].unique())


# Standardise PaymentMethod values
sales.loc[
    sales["PaymentMethod"] == "Paypal",
    "PaymentMethod"] = "PayPal"


# Verify PaymentMethod values
print(sales["PaymentMethod"].unique())

# Standardise Product values
sales.loc[sales["Product"] == "laptop",
          "Product"
] = sales.loc[
    sales["Product"] == "laptop",
    "Product"
    ].str.capitalize()

# Verify Product values
print(sales["Product"].unique())

# Correct invalid Quantity values
sales["Quantity"] = sales["Quantity"].mask(
    sales["OrderID"] == "ORD017", 
    3
)

sales["Quantity"] = sales["Quantity"].mask(
    sales["OrderID"] == "ORD020", 
    1
)

# Verify corrected Quantity values
print(
    sales.loc[
        sales["OrderID"] == "ORD017",
        ["OrderID","Quantity"]
   ]
)

print(
    sales.loc[
        sales["OrderID"] == "ORD020",
       ["OrderID", "Quantity"]
   ]
)

# Correct invalid Discount values
sales["Discount"] = sales["Discount"].mask(
    sales["OrderID"] == "ORD009", 
    20
)

sales["Discount"] = sales["Discount"].mask(
    sales["OrderID"] == "ORD019", 
     10
)

# Verify corrected Discount values
print(
    sales.loc[
        sales["OrderID"] == "ORD009",
        ["OrderID", "Discount"]
    ]
)

print(
    sales.loc[
        sales["OrderID"] == "ORD019",
        ["OrderID", "Discount"]
    ]
)

# Correct invalid OrderDate value
sales["OrderDate"] = sales["OrderDate"].mask(
    sales["OrderID"] == "ORD015",
    "18/06/2026"
)

# Verify corrected OrderDate value
print(
    sales.loc[
        sales["OrderID"] == "ORD015",
        ["OrderID", "OrderDate"]
    ]
)

# Convert OrderDate to datetime
sales["OrderDate"] = pd.to_datetime(
    sales["OrderDate"],
    format="%d/%m/%Y"
)

# Verify OrderDate data type
print(sales["OrderDate"].dtype)

# PRODUCTS DATA CLEANING
print("\n=== PRODUCT DATA CLEANING ===")

#  Standardise Category values
products["Category"] = products["Category"].replace(
    to_replace="Accessorise",
    value="Accessories"
)

# Verify Category values
print(products["Category"].unique())

# Remove duplicate rows
products.drop_duplicates(inplace=True)

# Verify duplicate rows were removed
print(products.duplicated().sum())

# Correct invalid UnitPrice value
products["UnitPrice"] = products["UnitPrice"].mask(products["UnitPrice"] == -140, 140)

# Verify corrected UnitPrice value
print(products.loc[products["Product"] == "External SSD", ["Product","UnitPrice"]])

print(products.loc[products["Category"] == "Accessories", ["Product","UnitPrice"]])

# Impute missing Keyboard UnitPrice with an assumed value of £70
products["UnitPrice"] = products["UnitPrice"].fillna(value=70,)

# Verify Keyboard UnitPrice
print(products.loc[products["Product"]=="Keyboard",["Product","UnitPrice"]])

# Standardise Product values
products["Product"] = products["Product"].replace(to_replace="Web Cam",value="Webcam")

# Verify Product values
print(products["Product"].unique())


# CLEANING VALIDATION
print("\n=== CLEANING VALIDATION ===")

# Verify no missing values remain
print(sales.isna().sum())
print(products.isna().sum())

# Verify no duplicate rows remain
print(sales.duplicated().sum())
print(products.duplicated().sum())

# Verify numeric values are within valid ranges
print(sales[sales["Quantity"] <= 0])
print(sales[(sales["Discount"] < 0) | (sales["Discount"] > 100)])
print(products[products["UnitPrice"] <= 0])

# Verify OrderDate data type
print(sales["OrderDate"].dtype)

# Verify all products in sales exist in the products dataset
print(sales[~sales["Product"].isin(products["Product"])])

# Save cleaned copys of the CSV files

sales.to_csv("data/cleaned/sales_clean.csv", index=False)
products.to_csv("data/cleaned/products_clean.csv", index=False)

# Verify CostPrice values are valid
print(products[products["CostPrice"] <= 0])

# Verify all ProductIDs in sales exist in the products dataset
print(
    sales[
        ~sales["ProductID"].isin(products["ProductID"])
    ]
)

# MERGE DATASET
print('\n ===MERGE DATASET===')


# Merge sales with product details using ProductID
sales_merged = sales.merge(
    products[["ProductID", "Category", "UnitPrice", "CostPrice"]],
    on="ProductID",
    how="left",
    validate="many_to_one"
)

# Verify the number of rows and columns after the merge
print(sales.shape)
print(sales_merged.shape)

# Inspect the merged dataset
print(sales_merged.head())

# Verify no missing values were introduced by the merge
print(
    sales_merged[
        ["Category", "UnitPrice", "CostPrice"]
    ].isna().sum()
)


# FEATURE CREATION
print('\ ===FEATURE CREATION')

# Calculate gross revenue before discounts
sales_merged["GrossRevenue"] = (
    sales_merged["Quantity"] * sales_merged["UnitPrice"]
)

# Verify GrossRevenue values
print(
    sales_merged[
        ["Product", "Quantity", "UnitPrice", "GrossRevenue"]
    ].head()
)


# Calculate discount amount
sales_merged["DiscountAmount"] = (
    (sales_merged["Discount"] / 100) * sales_merged["GrossRevenue"]
)

# Inspect GrossRevenue, Discount and DiscountAmount together
print(
    sales_merged[
        ["Product", "GrossRevenue", "Discount", "DiscountAmount"]
    ].head()
)

# Calculate net revenue after discounts
sales_merged["NetRevenue"] = (
    sales_merged["GrossRevenue"] - sales_merged["DiscountAmount"]
)

# Verify NetRevenue values
print(
    sales_merged[
        ["GrossRevenue", "DiscountAmount", "NetRevenue"]
    ].head()
)


# Calculate total cost of product sold
sales_merged["TotalCost"] = (
    sales_merged["CostPrice"] * sales_merged["Quantity"]
)

# Verify TotalCost values
print(
    sales_merged[
        ["Product", "Quantity", "TotalCost"]
    ].head()
)


# Calculate gross profit from each sale
sales_merged["GrossProfit"] = (
    sales_merged["NetRevenue"] - sales_merged["TotalCost"]
)

# Verify gross profit values
print(
    sales_merged[
        ["Product", "NetRevenue", "TotalCost", "GrossProfit"]
    ].head()
)


# Calculate profit margine from each sale
sales_merged["ProfitMargin"] = (
    sales_merged["GrossProfit"] / sales_merged["NetRevenue"] * 100
).round(2)

# Verify profit margin values
print(
    sales_merged[
        ["Product", "TotalCost", "GrossProfit", "ProfitMargin"]
    ].head()
)

print( sales_merged.head())

# Create a Year column from OrderDate
sales_merged["Year"] = sales_merged["OrderDate"].dt.year

# Verify Year values
print(
    sales_merged[
        ["OrderDate", "Year"]
    ].head()
)

# Create a MonthNumber column from OrderDate
sales_merged["MonthNumber"] = sales_merged["OrderDate"].dt.month

# Verify MonthNumber values
print(
    sales_merged[
        ["OrderDate", "MonthNumber"]
    ].head()
)

# Create a Month column from OrderDate
sales_merged["Month"] = sales_merged["OrderDate"].dt.month_name()

# Verify Month values
print(
    sales_merged[
        ["OrderDate", "MonthNumber", "Month"]
    ].head()
)

# Create a YearMonth column from OrderDate
sales_merged["YearMonth"] = sales_merged["OrderDate"].dt.to_period(freq="M")

# Verify YearMonth values
print(
    sales_merged[
        ["OrderDate", "YearMonth"]
    ].head()
)

# Create a HasDiscount column
sales_merged["HasDiscount"] = sales_merged["Discount"] > 0

# Verify HasDiscount values
print(
    sales_merged[
        ["Discount", "HasDiscount"]
    ].head()
)

# OVERALL KPI ANALYSIS
print('\ ===OVERALL KPI ANALISYS')

# Calculate total net revenue
Total_Net_Revenue = sales_merged["NetRevenue"].sum()

print(f"Total_Net_Revenue: £{Total_Net_Revenue:,.2f}")





