import matplotlib.pylot as plt 
import numpy as np 
from scipy.stats import linregress

pendapatan_rata_rata = np.array([5, 10, 20, 8, 4, 6, 12, 15])
penjualan_pizza = np.array([27, 46, 73, 40, 30, 28, 46, 59])

plt.scatter(pendapatan_rata_rata, penjualan_pizza)
plt.title('Scatter Diagram Penjualan Rata rata vs Penjualan Pizza')
plt.xlabel('Pendapatan Rata rata (1000$)')
plt.ylabel('Penjualan Pizza (1000 buah)')
plt.show()

correlation_coefficient = np.corrcoef(pendapatan_rata_rata, penjualan_pizza)[0 ,1]
print(f"Korelasi antara pendapatan rata rata dan penjualan pizza: {correlation_coefficient}")

slope, intercept, r_value, p_value, std_err = linregress(pendapatan_rata_rata, penjualan_pizza)

predicted_values = slope * pendapatan_rata_rata + intercept
SSR = np.sum((predicted_values - np.mean(penjualan_pizza))**2)
SSE = np.sum((penjualan_pizza -  predicted_values)**2)
SST = SSR + SSE
R_squared = SSR / SST 

print(f"slope: {slope}")
print(f"intercept: {intercept}")
print(f"SSR (Sum of Squared Regression) {SSR}")
print(f"SSE (Sum of Squared Error): {SSE}")
print(f"SST (Total Sum of Squared): {SST} ")
print(f"R-squared: {R_squared}")
