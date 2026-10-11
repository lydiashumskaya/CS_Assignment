import pandas as pd 
import matplotlib.pyplot as plt 

#seperating data 
df = pd.read_csv('istherecorrelation.csv', sep = ';', decimal = ',')
students = df['WO [x1000]']
beer = df['NL Beer consumption [x1000 hectoliter]']

#calculating pearson score 
r = students.corr(beer)

#plotting data 
for i in range(len(df)):
    plt.scatter(students.iloc[i], beer.iloc[i], label=df['Year'].iloc[i])
plt.xlabel('Number of WO students [x1000]')
plt.ylabel('NL Beer consumption [x1000 hectoliter]')
plt.title(f'Correlation between students and NL beer consumption. Pearson $r = {r:.3f}$')
plt.legend(title = 'Year', loc = 'upper left', fontsize = 6)
plt.savefig('correlation.png', dpi = 300)