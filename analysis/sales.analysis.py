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



# SALES DATA CLEANING

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