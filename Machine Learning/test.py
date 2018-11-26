import numpy as np
from scipy import stats

gdp = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1330167597.7653599, 1320670391.06145, 1379888268.15642, 1531843575.4189901, 1665363128.4916198, 1722798882.68156, 1873452513.96648, 1920262569.8324, 1941094972.0670397, 2021301675.97765, 2228279329.6089396, 2331005586.5921803, 2421474860.3352, 2623726256.9832397, 2791960893.85475, 2498932960.89385, 2467703910.61453, 2584463687.15084, None, None, None, None, None, None]
years = []
for i in range(0, 58):
    years.append(i)

array = np.column_stack((gdp, years))

gradient,intercept,r_value,p_value,std_err=stats.linregress(years,gdp)

print(gradient)
print(intercept)
