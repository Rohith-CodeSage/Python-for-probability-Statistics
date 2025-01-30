import numpy as np
import pandas as pd
data = [35,45,40,60,55,50,65,70,60,75,50,55,45,40,50]

median_numpy = np.median(data)
mode_numpy = np.unique(data, return_counts = True)
print(median_numpy," ",mode_numpy)

mode_pandas = pd.Series(data).mode()[0]
median_pandas = pd.Series(data).median()
 
print(mode_pandas, " ",median_pandas )


#for grpped data:
data1 = [25,30,35,40,45,50]
freq = [5,8,12,10,6,4]
df = pd.DataFrame({'Data': data1, 'Frequency': freq})
median = np.median(df['Data'])
mode = df['Data'].mode()[0]
print(median)
print(mode)


#cumulative frequency

"""
midean = L+((N/2-F)/f)*h

mode =  L+((f1 - f0)/2*f1-f0-f2)*h
"""

class_intervals = [(20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80)]
frequencies = [5, 8, 12, 10, 6, 4]

df = pd.DataFrame({
    'Class': class_intervals,
    'Frequency': frequencies
    })


df['Cumulative Frequency'] = df['Frequency'].cumsum()

median1  = np.median(df['Class'])
mode1 = df['Class'].mode()[0]

print(median1, "" , mode1)


data_class = {
    'class_intervals' : [(20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80)],
    'Frequency' : [5,8,12,10,6,4]

    }

df1 = pd.DataFrame(data)
print(df)
