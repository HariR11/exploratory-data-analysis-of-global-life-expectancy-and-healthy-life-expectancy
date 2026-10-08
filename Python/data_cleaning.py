#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning 
# This notebook contains the cleaning steps of the raw dataset.

# In[11]:


# Standardize column names

life.columns = life.columns.str.strip()
healthy.columns = healthy.columns.str.strip()

print("Column names standardized.")


# In[12]:


# checking numerical summary

print("Life expectancy numerical summary:")
print(life.describe())

print("\nHealthy life expectancy numerical summary:")
print(healthy.describe())


# In[13]:


# Clean the columns we will use as merge keys

life["GEO_NAME_SHORT"] = life["GEO_NAME_SHORT"].astype(str).str.strip()
healthy["GEO_NAME_SHORT"] = healthy["GEO_NAME_SHORT"].astype(str).str.strip()

life["DIM_SEX"] = life["DIM_SEX"].astype(str).str.strip().str.upper()
healthy["DIM_SEX"] = healthy["DIM_SEX"].astype(str).str.strip().str.upper()

life["DIM_TIME"] = pd.to_numeric(life["DIM_TIME"], errors="coerce")
healthy["DIM_TIME"] = pd.to_numeric(healthy["DIM_TIME"], errors="coerce")

print("Merge keys prepared.")


# In[14]:


# Checking duplicate rows before merging

print("Life expectancy duplicate rows:", life.duplicated().sum())
print("Healthy life expectancy duplicate rows:", healthy.duplicated().sum())


# In[15]:


# Merge life expectancy with healthy life expectancy
df = pd.merge(
    life,
    healthy,
    on=["GEO_NAME_SHORT", "DIM_TIME", "DIM_SEX"],
    how="inner",
    suffixes=("_life", "_healthy")
)

# Check merged data
print("Merged dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())


# In[16]:


#checking missing values
missing = df.isnull().sum()
print(missing)


# In[17]:


# Check missing values in all columns
missing = df.isnull().sum()

print(missing[missing > 0])


# In[18]:


# View rows with missing bounds
missing_bounds = df[
    df[[
        "AMOUNT_NL_life",
        "AMOUNT_NU_life",
        "AMOUNT_NL_healthy",
        "AMOUNT_NU_healthy"
    ]].isnull().any(axis=1)
]

print(missing_bounds[
    [
        "GEO_NAME_SHORT",
        "DIM_TIME",
        "DIM_SEX",
        "AMOUNT_N_life",
        "AMOUNT_NL_life",
        "AMOUNT_NU_life",
        "AMOUNT_N_healthy",
        "AMOUNT_NL_healthy",
        "AMOUNT_NU_healthy"
    ]
])


# In[19]:


# Check missing-bound observations
print(
    missing_bounds[
        ["GEO_NAME_SHORT", "DIM_TIME", "DIM_SEX"]
    ].to_string(index=False)
)


# In[20]:


# Check main analysis columns
print(df[
    [
        "GEO_NAME_SHORT",
        "DIM_TIME",
        "DIM_SEX",
        "AMOUNT_N_life",
        "AMOUNT_N_healthy"
    ]
].isnull().sum())


# In[21]:


# Check categorical values
print("Sex:")
print(df["DIM_SEX"].unique())

print("\nLife geographic type:")
print(df["DIM_GEO_CODE_TYPE_life"].unique())

print("\nHealthy geographic type:")
print(df["DIM_GEO_CODE_TYPE_healthy"].unique())

print("\nLife publish state:")
print(df["DIM_PUBLISH_STATE_CODE_life"].unique())

print("\nHealthy publish state:")
print(df["DIM_PUBLISH_STATE_CODE_healthy"].unique())


# In[22]:


# Count observations by geographic type
print(df["DIM_GEO_CODE_TYPE_life"].value_counts())


# In[23]:


# Check WHO region names
print(
    df.loc[df["DIM_GEO_CODE_TYPE_life"] == "WHOREGION",
           "GEO_NAME_SHORT"]
    .unique()
)


# In[24]:


# Check geographic type consistency
geo_type_match = (
    df["DIM_GEO_CODE_TYPE_life"] ==
    df["DIM_GEO_CODE_TYPE_healthy"]
)

print("Matching geographic types:", geo_type_match.all())
print("Mismatched rows:", (~geo_type_match).sum())


# In[25]:


# Check country/region name consistency
geo_name_match = (
    df["GEO_NAME_SHORT"] ==
    df["GEO_NAME_SHORT"]
)

print("Matching geographic names:", geo_name_match.all())


# In[26]:


# Count unique geographic names by type
print(
    df.groupby("DIM_GEO_CODE_TYPE_life")["GEO_NAME_SHORT"]
      .nunique()
)


# In[27]:


# Check duplicate country-year-sex rows
country_df = df[df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY"]

duplicates = country_df.duplicated(
    subset=["GEO_NAME_SHORT", "DIM_TIME", "DIM_SEX"]
).sum()

print("Duplicate country-year-sex rows:", duplicates)


# In[28]:


# Check missing values in main analysis columns
print(
    country_df[
        ["GEO_NAME_SHORT", "DIM_TIME", "DIM_SEX",
         "AMOUNT_N_life", "AMOUNT_N_healthy"]
    ].isna().sum()
)


# In[29]:


# Calculate the gap between life expectancy and healthy life expectancy
df["Health_Gap"] = (
    df["AMOUNT_N_life"] -
    df["AMOUNT_N_healthy"]
)

df[["AMOUNT_N_life", "AMOUNT_N_healthy", "Health_Gap"]].head()


# In[30]:


# Final check of the analysis columns
analysis_cols = [
    "GEO_NAME_SHORT",
    "DIM_TIME",
    "DIM_SEX",
    "AMOUNT_N_life",
    "AMOUNT_N_healthy",
    "Health_Gap"
]

print(df[analysis_cols].isna().sum())
print("\nDataset shape:", df.shape)


# In[31]:


# Define uncertainty-bound columns
bound_cols = [
    "AMOUNT_NL_life",
    "AMOUNT_NU_life",
    "AMOUNT_NL_healthy",
    "AMOUNT_NU_healthy"
]


# In[32]:


# Check missing-bound positions
for col in bound_cols:
    temp = df.sort_values(
        ["GEO_NAME_SHORT", "DIM_SEX", "DIM_TIME"]
    ).copy()

    temp["prev"] = temp.groupby(
        ["GEO_NAME_SHORT", "DIM_SEX"]
    )[col].shift(1)

    temp["next"] = temp.groupby(
        ["GEO_NAME_SHORT", "DIM_SEX"]
    )[col].shift(-1)

    print(f"\n{col}")
    print(
        temp[temp[col].isna()][
            ["GEO_NAME_SHORT", "DIM_TIME", "DIM_SEX", "prev", "next"]
        ]
    )


# In[33]:


# Check important analysis columns
analysis_cols = [
    "GEO_NAME_SHORT",
    "DIM_TIME",
    "DIM_SEX",
    "AMOUNT_N_life",
    "AMOUNT_N_healthy",
    "Health_Gap"
]

print(df[analysis_cols].isna().sum())


# In[34]:


# Columns with missing uncertainty-bound values
bound_cols = [
    "AMOUNT_NL_life",
    "AMOUNT_NU_life",
    "AMOUNT_NL_healthy",
    "AMOUNT_NU_healthy"
]

# Fill missing values with the median of each column
for col in bound_cols:
    df[col] = df[col].fillna(df[col].median())


# In[35]:


# Check missing values after filling
print(df[bound_cols].isna().sum())


# In[36]:


print(df.isna().sum())


# In[37]:


# Final verification of cleaned dataset

print("Final dataset shape:", df.shape)

print("\nTotal duplicate rows:", df.duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\nYears:")
print(sorted(df["DIM_TIME"].dropna().unique()))

print("\nSex categories:")
print(df["DIM_SEX"].unique())

print("\nGeographic types:")
print(df["DIM_GEO_CODE_TYPE_life"].unique())

print("\nNumber of countries:")
print(
    df.loc[
        df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY",
        "GEO_NAME_SHORT"
    ].nunique()
)


# In[86]:


# Perform a final quality check before saving the cleaned dataset.
print("FINAL DATASET CHECK")

print("Shape:", df.shape)

print("\nMissing values:")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

print("\nDuplicate rows:", df.duplicated().sum())

print("\nSex categories:")
print(df["DIM_SEX"].unique())

print("\nGeographic types:")
print(df["DIM_GEO_CODE_TYPE_life"].unique())

print("\nYears:")
print(sorted(df["DIM_TIME"].dropna().unique()))

print("\nNumber of countries:")
print(
    df.loc[
        df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY",
        "GEO_NAME_SHORT"
    ].nunique()
)

print("\nData types:")
print(df.dtypes)

# Save the final cleaned dataset.
df.to_csv(
    "Global_Life_Expectancy_Healthy_Life_Expectancy_Cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")


# In[87]:


# Save the final cleaned dataset.
df.to_csv(
    "Global_Life_Expectancy_Healthy_Life_Expectancy_Cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")

