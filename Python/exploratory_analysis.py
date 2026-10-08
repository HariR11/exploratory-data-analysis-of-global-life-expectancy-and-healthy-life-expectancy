#!/usr/bin/env python
# coding: utf-8

# # Exploratory Analysis
# 
# This notebook contains the statistical analysis, distributions, groupby calculations, percentages, relationships, and findings for Q1–Q10.

# ## Q1. How has life expectancy changed across countries from 2000 to 2021?

# In[40]:


#Average life expectancy by year

life = (
    df[
        (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
        (df["DIM_SEX"] == "TOTAL")
    ]
    .groupby("DIM_TIME")["AMOUNT_N_life"]
    .mean()
)

print("Average life expectancy by year:")
life


# In[41]:


# Country-level change in life expectancy from 2000 to 2021

life_change = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
    (df["DIM_SEX"] == "TOTAL") &
    (df["DIM_TIME"].isin([2000, 2021]))
][
    ["GEO_NAME_SHORT", "DIM_TIME", "AMOUNT_N_life"]
]

life_change_pivot = life_change.pivot(
    index="GEO_NAME_SHORT",
    columns="DIM_TIME",
    values="AMOUNT_N_life"
)

life_change_pivot["Change"] = (
    life_change_pivot[2021] -
    life_change_pivot[2000]
)

# Largest increase
life_change_pivot.sort_values(
    "Change", ascending=False
).head(10)


# In[43]:


# Calculating the change between 2000 and 2021

change = life.iloc[-1] - life.iloc[0]

print("Life expectancy in 2000:", round(life.iloc[0], 2))
print("Life expectancy in 2021:", round(life.iloc[-1], 2))
print("Overall change:", round(change, 2), "years")


# ## Q2. How has healthy life expectancy changed across countries from 2000 to 2021?

# In[45]:


#Average healthy life expectancy by year

healthy = (
    df[
        (df["DIM_GEO_CODE_TYPE_healthy"] == "COUNTRY") &
        (df["DIM_SEX"] == "TOTAL")
    ]
    .groupby("DIM_TIME")["AMOUNT_N_healthy"]
    .mean()
)

healthy


# In[46]:


# Country-level change in healthy life expectancy from 2000 to 2021

healthy_change = df[
    (df["DIM_GEO_CODE_TYPE_healthy"] == "COUNTRY") &
    (df["DIM_SEX"] == "TOTAL") &
    (df["DIM_TIME"].isin([2000, 2021]))
][
    ["GEO_NAME_SHORT", "DIM_TIME", "AMOUNT_N_healthy"]
]

healthy_change_pivot = healthy_change.pivot(
    index="GEO_NAME_SHORT",
    columns="DIM_TIME",
    values="AMOUNT_N_healthy"
)

healthy_change_pivot["Change"] = (
    healthy_change_pivot[2021] -
    healthy_change_pivot[2000]
)

healthy_change_pivot


# In[48]:


# Calculate the change between 2000 and 2021

change_healthy = healthy.iloc[-1] - healthy.iloc[0]

print("Healthy life expectancy in 2000:", round(healthy.iloc[0], 2))
print("Healthy life expectancy in 2021:", round(healthy.iloc[-1], 2))
print("Overall change:", round(change_healthy, 2), "years")


# ## Q3. Which countries had the highest and lowest life expectancy in the latest available year?

# In[50]:


#Life expectancy by country in 2021 
life_country = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
    (df["DIM_SEX"] == "TOTAL") &
    (df["DIM_TIME"] == 2021)
][
    ["GEO_NAME_SHORT", "AMOUNT_N_life"]
].sort_values(
    "AMOUNT_N_life",
    ascending=False
)

life_country


# In[51]:


#highest
print("Top 10 countries:")
life_country.head(10)


# In[52]:


#lowest
print("Bottom 10 countries:")
life_country.tail(10)


# ## Q4. Which countries had the highest and lowest healthy life expectancy in the latest available year?

# In[55]:


#Healthy life expectancy by country in 2021

healthy_country = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
    (df["DIM_SEX"] == "TOTAL") &
    (df["DIM_TIME"] == 2021)
][
    ["GEO_NAME_SHORT", "AMOUNT_N_healthy"]
].sort_values(
    "AMOUNT_N_healthy",
    ascending=False
)

healthy_country


# In[56]:


# highest 
print("Top 10 countries:")
healthy_country.head(10)


# In[57]:


#lowest
print("Bottom 10 countries")
healthy_country.tail(10)


# ## Q5. How does life expectancy differ between males and females across countries?

# In[60]:


#Compare life expectancy between males and females across countries in 2021

life_sex = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
    (df["DIM_SEX"].isin(["MALE", "FEMALE"])) &
    (df["DIM_TIME"] == 2021)
][
    ["GEO_NAME_SHORT", "DIM_SEX", "AMOUNT_N_life"]
]

life_sex


# In[61]:


# Reshape the data to compare male and female life expectancy for each country

life_sex_pivot = life_sex.pivot(
    index="GEO_NAME_SHORT",
    columns="DIM_SEX",
    values="AMOUNT_N_life"
)

life_sex_pivot


# In[62]:


# Calculate the difference between female and male life expectancy for each country

life_sex_pivot["Gap"] = (
    life_sex_pivot["FEMALE"] -
    life_sex_pivot["MALE"]
)

life_sex_pivot


# In[63]:


# Calculate the average life expectancy for males and females across all countries

sex_average = life_sex.groupby(
    "DIM_SEX"
)["AMOUNT_N_life"].mean()

sex_average


# In[64]:


# Calculate the average female-male life expectancy gap across countries

life_sex_pivot["Gap"].mean()


# ## Q6 — How does healthy life expectancy differ between males and females across countries?

# In[67]:


#Healthy life expectancy comparison between males and females in 2021

healthy_sex = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
    (df["DIM_SEX"].isin(["MALE", "FEMALE"])) &
    (df["DIM_TIME"] == 2021)
][
    ["GEO_NAME_SHORT", "DIM_SEX", "AMOUNT_N_healthy"]
]

healthy_sex


# In[68]:


# Average healthy life expectancy by sex

healthy_sex_average = healthy_sex.groupby("DIM_SEX")["AMOUNT_N_healthy"].mean()

print("Average healthy life expectancy by sex:")
healthy_sex_average


# In[69]:


# Calculate female-male healthy life expectancy gap

healthy_sex_pivot = healthy_sex.pivot(
    index="GEO_NAME_SHORT",
    columns="DIM_SEX",
    values="AMOUNT_N_healthy"
)

healthy_sex_pivot["Gap"] = (
    healthy_sex_pivot["FEMALE"] -
    healthy_sex_pivot["MALE"]
)

print("Average female-male healthy life expectancy gap:",
      healthy_sex_pivot["Gap"].mean())


# ## Q7 — What is the gap between life expectancy and healthy life expectancy across countries?

# In[72]:


#Gap between life expectancy and healthy life expectancy in 2021

health_gap = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
    (df["DIM_SEX"] == "TOTAL") &
    (df["DIM_TIME"] == 2021)
][
    ["GEO_NAME_SHORT", "AMOUNT_N_life", "AMOUNT_N_healthy", "Health_Gap"]
].sort_values(
    "Health_Gap",
    ascending=False
)

health_gap


# In[73]:


# Average gap between life expectancy and healthy life expectancy

average_health_gap = health_gap["Health_Gap"].mean()

print("Average health gap:",
      average_health_gap)


# In[74]:


# Minimum and maximum health gap

print("Largest health gap:",
      health_gap["Health_Gap"].max())

print("Smallest health gap:",
      health_gap["Health_Gap"].min())


# ## Q8 — Which countries have the largest and smallest gap between life expectancy and healthy life expectancy?

# In[77]:


#Countries with the largest and smallest health gaps in 2021

top_10_gap = health_gap.head(10)
bottom_10_gap = health_gap.tail(10)

plot_data = pd.concat([
    top_10_gap,
    bottom_10_gap
]).sort_values("Health_Gap")

plot_data[["GEO_NAME_SHORT", "Health_Gap"]]


# ## Q9 — How does life expectancy vary across different geographic regions?

# In[80]:


#Life expectancy across WHO regions in 2021

region_life = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "WHOREGION") &
    (df["DIM_SEX"] == "TOTAL") &
    (df["DIM_TIME"] == 2021)
][
    ["GEO_NAME_SHORT", "AMOUNT_N_life"]
]

region_life


# ## Q10 — What is the relationship between life expectancy and healthy life expectancy across countries?

# In[83]:


#Relationship between life expectancy and healthy life expectancy in 2021

relationship = df[
    (df["DIM_GEO_CODE_TYPE_life"] == "COUNTRY") &
    (df["DIM_SEX"] == "TOTAL") &
    (df["DIM_TIME"] == 2021)
][
    ["GEO_NAME_SHORT", "AMOUNT_N_life", "AMOUNT_N_healthy"]
]

relationship


# In[85]:


# Calculate correlation

correlation = relationship["AMOUNT_N_life"].corr(
    relationship["AMOUNT_N_healthy"]
)

print("Correlation:", correlation)

