import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#The file reading
df=pd.read_csv('housing.csv')
print(df)

df.shape
df.dtypes

#information about data
df.info()

#.What is the average median income of the data set and check the distribution of data using appropriate plots?
df["median_income"].mean()
df.hist(bins=50,color='purple')
plt.show()

#Draw an appropriate plot for housing_median_age
plt.hist(df['housing_median_age'],color='green')
plt.title('housing_median_age-Histogram_plot')
plt.xlabel('housing_median_age')
plt.ylabel('Frequencies')
plt.grid(True)
plt.show()

print(df['housing_median_age'].mean())
print(df['housing_median_age'].median())
print(df['housing_median_age'].std())

#Show with the help of visualization, how median_income and median_house_values are related?
sns.scatterplot(x='median_house_value',y='median_income',data=df,color='grey')
plt.show()

#Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.
df[df.isnull().any(axis=1)]
new_data=df.dropna(subset=["total_bedrooms"])
print(new_data)

#Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.
df['total_bedrooms']=df['total_bedrooms'].fillna(df['total_bedrooms'].mean())
print(df)

#Write a programming construct to calculate the median value of the data set wherever required
print(df.head())
print(df['longitude'].median())
print(df['latitude'].median())
print(df['housing_median_age'].median())
print(df['total_rooms'].median())
print(df['total_bedrooms'].median())
print(df['population'].median())
print(df['households'].median())
print(df['median_income'].median())
print(df['median_house_value'].median())

#Plot latitude versus longitude and explain your observations
sns.scatterplot(data=df,x='latitude',y='longitude',color='green')
plt.show()

#Create a data set for which the ocean_proximity is Near ocean
new_data=df.loc[df['ocean_proximity']=='NEAR OCEAN']
print(new_data)

#Find the mean and median of the median income for the data set created for above question?
print(new_data['median_income'].median())
print(new_data['median_income'].mean())

#Please create a new column named total_bedroom_size. If size 10 or less. It should be quoted as small. If the size is 11 or more but 1000 less, it should be medium, otherwise it should be large.
import numpy as np
conditions= [(df['total_bedrooms']<=10),
             (df['total_bedrooms'] >=11) & (df['total_bedrooms'] <=1000),
             (df['total_bedrooms']>1000)]
values=['small','medium','large']
df['total_bedroom-size']=np.select(conditions,values)
print(df)

sns.set_style("darkgrid")
sns.scatterplot(x="housing_median_age", y="population", hue="ocean_proximity",
                size="median_house_value", data=df)
plt.xlabel("housing_median_age")
plt.ylabel("population")
plt.title("housing_median_age - population According to ocean_proximity and median_house_value")
plt.show()


#see pairplot for relation between the variables
sns.pairplot(data=df, hue='ocean_proximity')
plt.show()

