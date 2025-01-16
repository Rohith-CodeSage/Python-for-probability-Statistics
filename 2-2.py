import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#  a = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [11, 12, 13, 14, 15, 16, 17, 18, 19], [15, 16, 17, 18, 19, 20, 21, 22, 23]])
#  print(a)
#  print()
#  print(a[2,:])
#  print()
#  print(a[:,0])
# print()
#  print(a[1,7])
#  print(a[2,-1])
# 
#  
#  x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
#  y = np.array([11,23,45,60,34,45,85,45,62,45,5,64,84,64,61,64,95,75,85,65])
#  plt.scatter(x,y)
#  plt.show()
# 
# Dataset = {
#     "state" : ['Telangana', 'Maharastra', 'Karnataka', 'Kerala', 'Tamil Nadu'],
#     "Captial" : ['Hyderabad', 'Mumbai', 'Benguluru', 'Tiruvananthanapuram', 'Chennai'],
#     "Literacy %" : [89,77,82,97,85],
#     "Avg High Temp(c)" : [33,30,29,31,32],
#     }
# 
# print(Dataset)
# print()
# df = pd.DataFrame(Dataset)
# 
# print(df)
#  plt.scatter(df['state'],df['Literacy %'])
#  plt.show()
# print()
# 
# print(df['state'])
#

a = {"Dist" : [15,13,16,15,16,17,14,15,16,16,17,14,17,17,16,14,15,16,15,14,13]}
df = pd.DataFrame(a)
print(df)

print("the number of elements  is = ", df['Dist'].size)

print()

df2 = pd.crosstab(index = df['Dist'], columns = 'Freq')
print(df2)

print(df2['Freq'].sum())

df2['Relative Freq'] = df2['Freq']/df2['Freq'].sum()
df2['Relative % Freq'] = df2['Freq']/df2['Freq'].sum()*100
df2.loc['Total'] = df2.sum()

