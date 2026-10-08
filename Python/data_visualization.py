#!/usr/bin/env python
# coding: utf-8

# # Data Visualization
# 
# This notebook contains the charts, heatmaps, plots, and geographic visualizations for Q1–Q10.

# ## Q1. How has life expectancy changed across countries from 2000 to 2021?

# In[42]:


# using matplot for visualize

plt.figure(figsize=(10, 5))

plt.plot(
    life.index,
    life.values,
    marker="o"
)

plt.title("Average Life Expectancy Across Countries (2000–2021)")
plt.xlabel("Year")
plt.ylabel("Average Life Expectancy (Years)")
plt.grid(True)

plt.show()


# ## Q2. How has healthy life expectancy changed across countries from 2000 to 2021?

# In[47]:


# using matplot for visualize
plt.figure(figsize=(10, 5))

plt.plot(
    healthy.index,
    healthy.values,
    marker="o"
)

plt.title("Average Healthy Life Expectancy Across Countries (2000–2021)")
plt.xlabel("Year")
plt.ylabel("Average Healthy Life Expectancy (Years)")
plt.grid(True)

plt.show()


# ## Q3. Which countries had the highest and lowest life expectancy in the latest available year?

# In[53]:


# using matplot for visualize
top_10 = life_country.head(10)
bottom_10 = life_country.tail(10)

plot_data = pd.concat([
    top_10,
    bottom_10
]).sort_values(
    "AMOUNT_N_life"
)

plt.figure(figsize=(10, 7))

plt.barh(
    plot_data["GEO_NAME_SHORT"],
    plot_data["AMOUNT_N_life"]
)

plt.title("Highest and Lowest Life Expectancy by Country (2021)")
plt.xlabel("Life Expectancy (Years)")
plt.ylabel("Country")

plt.show()


# ## Q4. Which countries had the highest and lowest healthy life expectancy in the latest available year?

# In[58]:


#using matplot for visualize
Top_10 = healthy_country.head(10)
Bottom_10 = healthy_country.tail(10)

plot_data = pd.concat([
    Top_10,
    Bottom_10
]).sort_values(
    "AMOUNT_N_healthy"
)

plt.figure(figsize=(10, 7))

plt.barh(
    plot_data["GEO_NAME_SHORT"],
    plot_data["AMOUNT_N_healthy"]
)

plt.title("Highest and Lowest Healthy Life Expectancy by Country (2021)")
plt.xlabel("Healthy Life Expectancy (Years)")
plt.ylabel("Country")

plt.show()


# ## Q5. How does life expectancy differ between males and females across countries?

# In[65]:


#using matplot for visulize
plt.figure(figsize=(7, 5))

sex_average.plot(kind="bar")

plt.title("Average Life Expectancy by Sex (2021)")
plt.xlabel("Sex")
plt.ylabel("Life Expectancy (Years)")
plt.xticks(rotation=0)

plt.show()


# ## Q6 — How does healthy life expectancy differ between males and females across countries?

# In[70]:


# using matplot for visualize

plt.figure(figsize=(7, 5))

healthy_sex_average.plot(kind="bar")

plt.title("Average Healthy Life Expectancy by Sex (2021)")
plt.xlabel("Sex")
plt.ylabel("Healthy Life Expectancy (Years)")
plt.xticks(rotation=0)

plt.show()


# ## Q7 — What is the gap between life expectancy and healthy life expectancy across countries?
# 

# In[75]:


# using matplot for visualize 

plt.figure(figsize=(8, 5))

plt.hist(
    health_gap["Health_Gap"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Life Expectancy–Healthy Life Expectancy Gap (2021)")
plt.xlabel("Health Gap (Years)")
plt.ylabel("Number of Countries")

plt.show()


# ## Q8 — Which countries have the largest and smallest gap between life expectancy and healthy life expectancy?

# In[78]:


#using matplot for visualize

plt.figure(figsize=(10, 7))

plt.barh(
    plot_data["GEO_NAME_SHORT"],
    plot_data["Health_Gap"]
)

plt.title("Countries with the Largest and Smallest Health Gap (2021)")
plt.xlabel("Health Gap (Years)")
plt.ylabel("Country")

plt.show()


# ## Q9 — How does life expectancy vary across different geographic regions?

# In[81]:


#using matplot for visualize

plt.figure(figsize=(10, 6))

plt.stem(
    region_life["GEO_NAME_SHORT"],
    region_life["AMOUNT_N_life"]
)

plt.title("Life Expectancy Across WHO Regions (2021)")
plt.xlabel("WHO Region")
plt.ylabel("Life Expectancy (Years)")
plt.xticks(rotation=30)

plt.show()


# ## Q10 — What is the relationship between life expectancy and healthy life expectancy across countries?

# In[84]:


# using matplot for visualize

plt.figure(figsize=(8, 6))

plt.scatter(
    relationship["AMOUNT_N_life"],
    relationship["AMOUNT_N_healthy"]
)

plt.title("Relationship Between Life Expectancy and Healthy Life Expectancy (2021)")
plt.xlabel("Life Expectancy (Years)")
plt.ylabel("Healthy Life Expectancy (Years)")

plt.show()

