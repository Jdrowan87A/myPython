import numpy as np 
import pandas as pd 
import matplotlib.pylab as plt
import scipy as sp 

df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv")

print(df)

t = np.linspace(0, 1, 100)
plt.plot(t,t**2)
plt.show()

