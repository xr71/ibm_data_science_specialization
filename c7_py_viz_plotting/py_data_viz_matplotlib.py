import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')

df_can.head() 

yr_list = list(map(str, range(1980, 2014)))

df_can_haiti = df_can.loc[df_can.OdName == 'Haiti']
df_can_haiti = df_can_haiti.loc[:, list(range(1980, 2014))]

df_can_haiti_t = df_can_haiti.transpose()

df_can_haiti_t.plot()

# histograms
c, e = np.histogram(df_can_haiti_t)
df_can_haiti_t.plot(kind="hist")
df_can_haiti_t.plot(kind="hist", xticks=e)

