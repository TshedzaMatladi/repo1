# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

# Load the data
file_path = "movie_dataset.csv"
df = pd.read_csv(file_path)
df.info()
# Remove spaces from column names
#df.columns = df.columns.str.strip()

# Handling missing values - Assuming filling missing revenue with the mean
df['Revenue (Millions)'] = pd.to_numeric(df['Revenue (Millions)'], errors='coerce')
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean(), inplace=True)

# Now let's proceed to answer the quiz questions

# Question 1: What is the highest-rated movie in the dataset?
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]['Title'].values[0]
print (highest_rated_movie)

# Question 2: What is the average revenue of all movies in the dataset?
average_revenue = df['Revenue (Millions)'].mean()
print(average_revenue)

# Question 3: What is the average revenue of movies from 2015 to 2017 in the dataset?
average_revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue (Millions)'].mean()

# Question 4: How many movies were released in the year 2016?
movies_2016 = df[df['Year'] == 2016].shape[0]

# Question 5: How many movies were directed by Christopher Nolan?
movies_nolan = df[df['Director'] == 'Christopher Nolan'].shape[0]

# Question 6: How many movies in the dataset have a rating of at least 8.0?
high_rated_movies = df[df['Rating'] >= 8.0].shape[0]

# Question 7: What is the median rating of movies directed by Christopher Nolan?
median_rating_nolan = df[df['Director'] == 'Christopher Nolan']['Rating'].median()

# Question 8: Find the year with the highest average rating?
year_highest_avg_rating = df.groupby('Year')['Rating'].mean().idxmax()

# Question 9: What is the percentage increase in the number of movies made between 2006 and 2016?
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

# Question 10: Find the most common actor in all the movies?
most_common_actor = df['Actors'].str.split(', ').explode().mode()[0]

# Question 11: How many unique genres are there in the dataset?
unique_genres_count = df['Genre'].str.split(', ').explode().nunique()

# Question 12: Do a correlation of the numerical features, what insights can you deduce?

import seaborn as sns
import matplotlib.pyplot as plt
## Select only numerical columns for correlation analysis

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
numerical_features_df = df[numerical_columns]

# Calculate the correlation matrix
correlation_matrix = numerical_features_df.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Print insights based on correlation values
print("\nInsights:")
print(correlation_matrix.unstack().sort_values(ascending=False).drop_duplicates().head(6))

#Create a heatmap using Seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True,cmap ='coolwarm', linewidths=.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()