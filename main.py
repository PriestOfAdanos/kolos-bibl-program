import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Stworzenie ramki danych na podstawie dostarczonych danych
data = {
    'Rok': [1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022],
    'Wzrost PKB': [1.5, 3.8, 5.2, 7.0, 6.0, 6.8, 4.8, 4.1, 4.0, 1.0, 1.4, 3.8, 5.3, 3.5, 6.2, 6.7, 4.9, 1.8, 3.8, 5.0, 1.6, 1.4, 3.3, 3.8, 2.9, 4.8, 5.3, 4.1, -2.7, 6.9, 5.1]
}

df = pd.DataFrame(data)

# Wyświetlanie lat, w których wzrost PKB był największy i najmniejszy
print(df.loc[df['Wzrost PKB'].idxmax()]['Rok'])
print(df.loc[df['Wzrost PKB'].idxmin()]['Rok'])

# Tworzenie wykresu słupkowego z ostatnich pięciu lat
plt.bar(df['Rok'].tail(5), df['Wzrost PKB'].tail(5))
plt.show()

# Sortowanie lat w porządku malejącym wzrostu PKB
df_sorted = df.sort_values('Wzrost PKB', ascending=False)

# Tworzenie słownika z latami jako kluczami i wartościami wzrostu PKB
pkb_dict = df.set_index('Rok')['Wzrost PKB'].to_dict()

# Tworzenie wykresu z pięciu lat o największym wzroście PKB
top_5_years = df_sorted.head(5)['Rok']
top_5_gdp = df_sorted.head(5)['Wzrost PKB']
plt.bar(top_5_years, top_5_gdp)
plt.show()

# Tworzenie wykresów kołowych dla ostatnich pięciu lat
fig, axs = plt.subplots(1, 2)
axs[0].pie(df['Wzrost PKB'].tail(5), labels=df['Rok'].tail(5), autopct='%1.1f%%')
axs[1].pie(df['Wzrost PKB'].tail(5), labels=df['Rok'].tail(5), autopct='%1.1f%%')
plt.show()
