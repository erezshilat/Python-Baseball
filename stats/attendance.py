import pandas as pd
import matplotlib.pyplot as plt
from data import games

attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance') , ['multi3','year']]
attendance.columns = ['attendance', 'year']
vals = attendance['attendance']
attendance['attendance'] = pd.to_numeric(vals.tolist(), errors ='ignore')
attendance.plot(x='year', y='attendance', kind='bar')
plt.xlabel('Year')
plt.ylabel('Attendence')
plt.axhline(y = attendance['attendance'].mean(), color="green", linestyle="dashed")
plt.show()
