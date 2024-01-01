

import pandas as pd
import plotly.express as px

pd.options.display.float_format = '{:,.2f}'.format

# Read the CSV file and display its shape
df_apps=pd.read_csv('apps.csv')
print(df_apps.shape)

# Display the first few rows and a sample of 5 rows
print(df_apps.head())
print(df_apps.sample(5))

# Drop unnecessary columns
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1, inplace=True)

# Display the first few rows after dropping columns
print(df_apps.head())

# Identify and drop rows with missing values in the 'Rating' column
nan_rows = df_apps[df_apps.Rating.isna()]
print(nan_rows.shape)
print(nan_rows.head())
df_apps_clean = df_apps.dropna()

# Display the cleaned DataFrame shape
print(df_apps_clean.shape)

# Identify and drop duplicated rows
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
print(duplicated_rows.head())
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])

# Display the cleaned DataFrame shape after removing duplicates
print(df_apps_clean.shape)

# Display the top apps by rating, size, and reviews
print(df_apps_clean.sort_values('Rating', ascending=False).head())
print(df_apps_clean.sort_values('Size_MBs', ascending=False).head())
print(df_apps_clean.sort_values('Reviews', ascending=False).head(50))

# Create a pie chart for Content Rating
ratings = df_apps_clean.Content_Rating.value_counts()
fig = px.pie(labels=ratings.index, values=ratings.values, title="Content Rating", names=ratings.index, hole=0.6)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
fig.show()

# Clean and analyze the 'Installs' column
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs.str.replace(',', ''))

# Clean and analyze the 'Price' column
df_apps_clean.Price = pd.to_numeric(df_apps_clean.Price.str.replace('$', ''))

# Display the top apps by price after cleaning
print(df_apps_clean.sort_values('Price', ascending=False).head(20))

# Filter out apps with price above $250
df_apps_clean = df_apps_clean[df_apps_clean['Price'] < 250]
print(df_apps_clean.sort_values('Price', ascending=False).head(5))

# Calculate and display the top apps by estimated revenue
df_apps_clean['Revenue_Estimate'] = df_apps_clean.Installs.mul(df_apps_clean.Price)
print(df_apps_clean.sort_values('Revenue_Estimate', ascending=False)[:10])

# Analyze and visualize the number of apps per category
print(df_apps_clean.Category.nunique())
top10_category = df_apps_clean.Category.value_counts()[:10]

bar = px.bar(x=top10_category.index, y=top10_category.values)
bar.show()

# Visualize category popularity using horizontal bar chart
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

h_bar = px.bar(x=category_installs.Installs, y=category_installs.index, orientation='h', title='Category Popularity')
h_bar.update_layout(xaxis_title='Number of Downloads', yaxis_title='Category')
h_bar.show()

# Analyze and visualize app concentration in categories
cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})
cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how="inner")
print(f'The dimensions of the DataFrame are: {cat_merged_df.shape}')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = px.scatter(cat_merged_df, x='App', y='Installs', title='Category Concentration', size='App',
                     hover_name=cat_merged_df.index, color='Installs')
scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)", yaxis_title="Installs",
                      yaxis=dict(type='log'))
scatter.show()

# Analyze and visualize top app genres
print(len(df_apps_clean.Genres.unique()))
num_genres = df_apps_clean.Genres.str.split(';', expand=True).stack().value_counts()

bar = px.bar(x=num_genres.index[:15], y=num_genres.values[:15], title='Top Genres',
             hover_name=num_genres.index[:15], color=num_genres.values[:15], color_continuous_scale='Agsunset')
bar.update_layout(xaxis_title='Genre', yaxis_title='Number of Apps', coloraxis_showscale=False)
bar.show()

# Analyze and visualize distribution of app types (Free vs Paid)
print(df_apps_clean.Type.value_counts())
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})
df_free_vs_paid.sort_values('App')

g_bar = px.bar(df_free_vs_paid, x='Category', y='App', title='Free vs Paid Apps by Category', color='Type',
               barmode='group')
g_bar.update_layout(xaxis_title='Category', yaxis_title='Number of Apps', xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))
g_bar.show()

# Analyze and visualize the distribution of downloads for Paid Apps
box = px.box(df_apps_clean, y='Installs', x='Type', color='Type', notched=True, points='all',
             title='How Many Downloads are Paid Apps Giving Up?')
box.update_layout(yaxis=dict(type='log'))
box.show()

# Analyze and visualize revenue and price for Paid Apps per category
df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps, x='Category', y=['Revenue_Estimate', 'Price'], title='Revenue and Price for Paid Apps')
box.update_layout(xaxis_title='Category', yaxis_title='Values (log scale)', xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))
box.show()
