import numpy as np

"""
formulas = {

# mean = Exi/n
# mean for grped data = Exifi/Efi
# mean for grped data class => class = class = (0-10)(10-20)(20-30) ///freq = Efimi/Efi ////mi = mid point = (start+end)/2
}
"""

# mean by maths
data = [85, 92, 78, 89, 95, 87, 90]
mean = sum(data)/len(data)
print(mean)

#using numpy
arr = np.array(data)
mean1 = arr.mean()
print(mean1)

#using pandas
import pandas as pd
data_series = pd.Series(data)
print(data_series)
mean11 = data_series.mean()
print(mean11)
    

# mean for grped data   
age = [15, 16, 17, 18, 19, 20]
freq = [2, 5, 11, 9, 14, 13]
mean2 = 0
freq1 =0
for i in range(len(age)):
    mean2 += age[i] * freq[i]
    freq1 += freq[i]
mean2 = mean2 / freq1
print(mean2)

#another method
sum_fx = sum(f*x for f,x in zip(freq,age))
print(sum_fx)
sum_f = sum(freq)
print(sum_f)
mean_again = sum_fx/sum_f
print(mean_again)


#using arrays
age_array = np.array(age)
freq_array = np.array(freq)
sum_fx_array = np.sum(age_array*freq_array)
sum_f_array = np.sum(freq_array)
print(sum_fx_array/sum_f_array)

#using pandas
df = pd.DataFrame({'age':age,'freq':freq})
print(df)
sum_fx_pandas = (df['age']*df['freq']).sum()
print(sum_fx_pandas)
sum_f_pandas = (df['freq']).sum()
print(sum_f_pandas)
print(sum_fx_pandas/sum_f_pandas)


#mean for class grped data

class_int = [(0,10),(10,20),(20,30),(30,40),(40,50),(50,50)]
freq_class = [12,18,27,20,17,6]
midpoint = [(start+end)/2 for start, end in class_int]
print(midpoint)

sum_fm_class = sum(f*x for f,x in zip(freq_class,midpoint))
print(sum_fm_class)
sum_f_class = sum(freq_class)
print(sum_fm_class/sum_f_class)


#using numpy
import numpy as np
midpoint=[(start+end)/2 for start, end in class_int]
x=np.array(class_int)
y=np.array(freq_class)
z=np.array(midpoint)
sum_fm=np.sum(y*z)
print(sum_fm)
sum_f=np.sum(y)
print(sum_f)
print(sum_fm/sum_f)

#using pandas

import pandas as pd
class_int=[(0,10),(10,20),(20,30),(30,40),(40,50),(50,50)]
freq=[12,18,27,20,17,6]
df=pd.DataFrame({'class':class_int,'freq':freq})
print(df)
df['midpoint']=df['class'].apply(lambda interval:interval[0]+interval[1]/2)
df['fimi']=df['midpoint']*df['freq']
totals={
    'class':'Total',
    'freq':df['freq'].sum(),
    'midpoint':' ',
    'fimi':df['fimi'].sum(),
    }

df=pd.concat([df,pd.DataFrame([totals])],ignore_index=True)
print(df)
mean=df['fimi'].iloc[-1]/df['freq'].iloc[-1]
print(df)
print('The mean of the data',mean)