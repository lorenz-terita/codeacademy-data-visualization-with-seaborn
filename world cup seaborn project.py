import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv('WorldCupMatches.csv')
df['Total Goals']= df['Home Team Goals']+ df['Away Team Goals']
plt.barplot(df['year'], df['Total Goals'])
sns.set_style('whitegrid')
sns.set_context("poster", font_scale=1)
f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(x=df['Year'], y=df['Total Goals'])
ax.set_title('goals per year')
plt.show()

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())
sns.set_context('notebook', font_scale = 1.25)
f, ax2 =plt.figure(figsize=(12,7))
ax2 = sns.boxplot(x ='year', y='goals', data= df_goals, palette= 'Spectral')
ax2.set_title('home team goals per year')
plt.show()
