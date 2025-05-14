import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('Happiness-data.csv')

# Group by country and year
happiness_by_year = df.groupby(['Country name', 'Year'])['Life Ladder'].mean().reset_index()

# Create the plot
plt.figure(figsize=(15, 8))

# Plot each country's happiness trend
for country in happiness_by_year['Country name'].unique():
    country_data = happiness_by_year[happiness_by_year['Country name'] == country]
    plt.plot(country_data['Year'], country_data['Life Ladder'], 
            label=country, alpha=0.5, linewidth=1)

# Customize the plot
plt.title('Happiness Trends by Country Over Time', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend with a scrollbar if there are many countries
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plt.savefig('happiness_by_country_year.png', dpi=300, bbox_inches='tight')
plt.close()

# Print summary statistics
print("\nHappiness Statistics by Country:")
print("==============================")
country_stats = happiness_by_year.groupby('Country name')['Life Ladder'].agg(['mean', 'min', 'max', 'std']).round(3)
print(country_stats.sort_values('mean', ascending=False))

# Group by year and country, calculate mean happiness score
happiness_by_year_country = df.groupby(['Year', 'Country name'])['Life Ladder'].mean().reset_index()

# Sort by year and happiness score
happiness_by_year_country = happiness_by_year_country.sort_values(['Year', 'Life Ladder'], ascending=[True, False])

# Print the results
print("\nHappiness Scores by Year and Country:")
print("=====================================")
for year in sorted(happiness_by_year_country['Year'].unique()):
    print(f"\nYear {year}:")
    year_data = happiness_by_year_country[happiness_by_year_country['Year'] == year]
    print(year_data[['Country name', 'Life Ladder']].to_string(index=False))

# Create a visualization of top 10 happiest countries for each year
plt.figure(figsize=(15, 8))
for year in sorted(df['Year'].unique()):
    year_data = df[df['Year'] == year]
    top_10 = year_data.nlargest(10, 'Life Ladder')
    plt.plot([year] * 10, top_10['Life Ladder'], 'o', label=f'Top 10 {year}')

plt.title('Top 10 Happiest Countries by Year')
plt.xlabel('Year')
plt.ylabel('Happiness Score')
plt.legend()
plt.grid(True)
plt.savefig('happiness_trends.png')
plt.close()

# Calculate average happiness by year
yearly_avg = df.groupby('Year')['Life Ladder'].mean()

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg.index, yearly_avg.values, marker='o', linestyle='-', linewidth=2, markersize=8)

# Customize the plot
plt.title('Average Global Happiness Score by Year', fontsize=14, pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Happiness Score', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add value labels on the points
for x, y in zip(yearly_avg.index, yearly_avg.values):
    plt.text(x, y, f'{y:.2f}', ha='center', va='bottom')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plt.savefig('happiness_by_year.png', dpi=300, bbox_inches='tight')
plt.close()

# Print the yearly averages
print("\nAverage Happiness by Year:")
print("=========================")
print(yearly_avg.round(3)) 