# %%
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tips.csv")

gender_counts = data['sex'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(gender_counts, 
        labels=gender_counts.index, 
        autopct='%1.1f%%',     
        startangle=90,        
        colors=['#66b3ff', '#ff9999'],
        explode=(0.05, 0),       
        shadow=True)

plt.title("Persentase Laki-laki dan Perempuan yang Memberikan Tips")
plt.axis('equal') 
plt.show()
# %%

# %%
# Visualisasi rata-rata tip berdasarkan hari (Insight baru)
avg_tip_per_day = data.groupby('day')['tip'].mean()

plt.figure(figsize=(8, 5))
avg_tip_per_day.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-rata Tip yang Diberikan Berdasarkan Hari')
plt.xlabel('Hari')
plt.ylabel('Rata-rata Tip ($)')
plt.xticks(rotation=45)
plt.show()
# %%

# %%
# Tugas: Visualisasi Insight Model Data Lain
# Melihat hubungan antara Total Bill dan Tip (Scatter Plot)
plt.figure(figsize=(10, 6))
plt.scatter(data['total_bill'], data['tip'], color='purple', alpha=0.6)

plt.title("Hubungan antara Total Tagihan dan Besaran Tip") 
plt.xlabel("Total Tagihan ($)") 
plt.ylabel("Tip ($)") 
plt.grid(True, linestyle='--', alpha=0.5)

plt.show() 
# %%