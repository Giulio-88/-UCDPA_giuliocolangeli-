#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[39]:


#import a csv file into a Pandas Dataframe related to the equipment lost by the russian Army in 106 days of war - from 25/02/22 till 10/06/22
ru_equip_losses = pd.read_csv(r'C:\Users\giulio.colangeli\OneDrive - Accenture\AGS\Giulio\Data Analytics for Business\Assessment\UCDPA_giuliocolangeli\russia_losses_equipment.csv')

#import a csv file into a Pandas Dataframe related to the personnel lost by the russian Army in 106 days of war - from 25/02/22 till 10/06/22
ru_pers_losses = pd.read_csv(r'C:\Users\giulio.colangeli\OneDrive - Accenture\AGS\Giulio\Data Analytics for Business\Assessment\UCDPA_giuliocolangeli\russia_losses_personnel.csv')


# In[40]:


ru_equip_losses.head()


# In[41]:


ru_pers_losses.head()


# In[77]:


#checking for null data ru_equip_losses
ru_equip_losses.isna().sum()
#Remove NaN
ru_equip_losses.dropna().fillna(0)


# In[46]:


#checking for null data ru_pers_losses
ru_pers_losses.isna().sum()


# In[47]:


#Info related to russian equipment:
#106 total entries
#Date is "object" Dtype, change to DateTime
#Some data are in float64, convert to Int
ru_equip_losses.info()


# In[48]:


#Replace NaN data with 0 ru_equip_losses and convert data as Int
ru_equip_losses.fillna(0, inplace = True)
ru_equip_losses['military auto'] = ru_equip_losses['military auto'].astype(int)
ru_equip_losses['fuel tank'] = ru_equip_losses['fuel tank'].astype(int)
ru_equip_losses['special equipment'] = ru_equip_losses['special equipment'].astype(int)
ru_equip_losses['mobile SRBM system'] = ru_equip_losses['mobile SRBM system'].astype(int)
ru_equip_losses['vehicles and fuel tanks'] = ru_equip_losses['vehicles and fuel tanks'].astype(int)
ru_equip_losses['cruise missiles'] = ru_equip_losses['cruise missiles'].astype(int)


# In[49]:


ru_equip_losses.isna().sum()


# In[50]:


#There are 106 rows and 18 columns in ru_equip_losses
ru_equip_losses.shape


# In[51]:


pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[52]:


print(ru_equip_losses)


# In[53]:


#Change Date from "object" to DateTime in ru_equip_losses
ru_equip_losses['date'] = pd.to_datetime(ru_equip_losses['date'])
ru_equip_losses.info()


# In[54]:


#Drop Date Duplicates
df=ru_equip_losses.drop_duplicates(subset=["date"])
print(df)


# In[55]:


#Set Date & Day as Index and sorting descending
date_day = df.set_index(["date","day"]).sort_index(level=["date", "day"], ascending = False)
print(date_day)


# In[56]:


date_day.describe()


# In[57]:


#Create a dictionary list to calculate what is the max of lost equipment since the beginning of the war
max_equip_lost_dict = {"equipment":['aircraft_losses', 'helicopter_losses', 'tank_losses', 'APC_losses', 'field_artillery_losses',
                                   'MRL_losses', 'ma_losses','fuel_tank_losses', 'drone_losses', 'naval_ship_losses', 'anti_aircraft_warfare_losses',
                                   'special_equipment_losses', 'SRBM_losses', 'vf_losses', 'cruise_missiles_losses'],
                       "values":[212, 178, 1409, 3450, 712,222, 1701, 76, 572, 13, 97, 54, 4, 2438, 125]}
print(max_equip_lost_dict)


# In[58]:


#Create a DataFrame to reflect the dictionary list created.
max_equip_lost = pd.DataFrame(max_equip_lost_dict)
print(max_equip_lost)


# In[59]:


#Calculate the average of lost equipments by day
#aircraft
aircraft_per_day = np.divide(212,106)
print('avg_aricraft_lost_per_day =',aircraft_per_day)

#helicopter
helicopter_per_day = np.divide(178, 106)
print('avg_helicopter_lost_per_day =',helicopter_per_day)

#tank
tank_per_day = np.divide(1409, 106)
print('avg_tank_lost_per_day =',tank_per_day)

#APC
APC_per_day = np.divide(3450, 106)
print('avg_APC_lost_per_day =',APC_per_day)

#field artillery
field_artillery_lost_per_day = np.divide(712, 106)
print('avg_field_artillery_lost_per_day =',field_artillery_lost_per_day)

#MRL
MRL_lost_per_day = np.divide(222, 106)
print('avg_MRL_lost_per_day =',MRL_lost_per_day)

#fuel tank
fuel_tank_per_day = np.divide(76, 106)
print('avg_fuel_tank_lost_per_day =',fuel_tank_per_day)

#drone
drone_per_day = np.divide(572, 106)
print('avg_drone_lost_per_day =',drone_per_day)

#naval ship
naval_ship_per_day = np.divide(13, 106)
print('avg_naval_ship_lost_per_day =',naval_ship_per_day)

#anti-aircraft warfare
anti_aircraft_warfare_per_day = np.divide(97, 106)
print('avg_anti_aricraft_warfare_lost_per_day =',anti_aircraft_warfare_per_day)

#special equipment
special_equipment_per_day = np.divide(54, 106)
print('avg_special_equipment_lost_per_day =',special_equipment_per_day)

#SRBM
SRBM_per_day = np.divide(4, 106)
print('avg_SRBM_lost_per_day =',SRBM_per_day)

#vf
vf_per_day = np.divide(2438, 106)
print('avg_vf_lost_per_day =',vf_per_day)

#cruise missiles
cruise_missiles_per_day = np.divide(125, 106)
print('avg_cruise_missiles_lost_per_day =',cruise_missiles_per_day)


# In[60]:


#Calculate what is the equipment loss the russian army suffered the most since the beginning of the war

equip_lost_avg = [["aircraft_lost_per_day", 2.0, 106],
                  ["helicopter_lost_per_day",1.179245283018868, 106],
                  ["tank_lost_per_day",13.29245283018868, 106],
                  ["APC_lost_per_day", 32.54716981132076, 106],
                  ["MRL_lost_per_day", 6.716981132075472, 106],
                ["field_artillery_lost_per_day",2.0943396226415096, 106],
                  ["fuel_tank_lost_per_day", 0.7169811320754716, 106],
                  ["drone_lost_per_day", 5.39622641509434, 106],
                  ["naval_ship_lost_per_day", 0.12264150943396226, 106],
                ["anti_aircraft_warfare_lost_per_day", 0.9150943396226415, 106],
                ["special_equipment_lost_per_day", 0.5094339622641509, 106],
                ["SRBM_lost_per_day", 0.03773584905660377, 106],
                ["vf_lost_per_day", 23.0, 106],
                ["cruise_missiles_lost_per_day", 1.179245283018868, 106]] 
                  
                  
#transform it in DataFrame
equip_lost_avg =pd.DataFrame(equip_lost_avg, columns = ["avg_equip", "avg", "total days"])

print(equip_lost_avg)
        
    
    
        
    


# In[61]:


#looping, interrows
for index, row in equip_lost_avg.iterrows():

    print(row["avg_equip"])
   


# In[62]:


#Conditional statement to check what is the equpiment the russian army lost the most
the_most_lost_equip = pd.DataFrame.from_dict( {'equip':['aircraft_lost_per_day','helicopter_lost_per_day', 'tank_lost_per_day',
                                'APC_lost_per_day', 'field_artillery_lost_per_day', 'MRL_lost_per_day',
                              'fuel_tank_lost_per_day', 'drone_lost_per_day', 'naval_ship_lost_per_day', 'anti_aircraft_warfare_lost_per_day',
                               'special_equipment_lost_per_day', 'SRBM_lost_per_day', 'vf_lost_per_day', 'cruise_missiles_lost_per_day'],
                      'avg_equip':[2.0, 1.679245283018868, 13.29245283018868, 32.54716981132076, 6.716981132075472, 2.0943396226415096,
                                 0.7169811320754716, 5.39622641509434, 0.12264150943396226, 0.9150943396226415, 0.5094339622641509,
                                   0.03773584905660377, 23.0, 1.179245283018868]})


the_most_lost_equip.loc[the_most_lost_equip['avg_equip'] > 30, 'Over 30'] = 'X'
the_most_lost_equip.loc[the_most_lost_equip['avg_equip'] < 30, 'Over 30'] = ''
print(the_most_lost_equip)



# In[63]:


#From the statement provided the russian army lost 'APC - Armoured Personnell carrier' more than any other equipment

print(date_day)


# In[64]:


#groupby the number of aircraft lost
av_t = date_day[['cruise missiles', 'aircraft', 'helicopter','drone']] = date_day[['cruise missiles', 'aircraft', 'helicopter','drone']].apply(pd.to_numeric)
av_t2 = date_day.drop_duplicates(['aircraft'])
av_t2.groupby(['date'])['aircraft'].sum()
av_t2.pivot_table(values = ['aircraft'], index='date')


# In[65]:


#Graph to show the amount of aircraft lost since the beginning of the war
date = ['25 February', '25 March', '25 April', '25 May', '10 June']
aircraft = [10, 115, 181, 205, 212]
plt.figure(figsize=(15,7))
plt.title ('Aircraft Lost')
plt.plot(date, aircraft)
plt.show


# In[66]:


#Equipment loss per a day graph
#list_1 = the_most_lost_equip.set_index(the_most_lost_equip['equip']).stack().reset_index(level=1, drop = True);
list_1 = the_most_lost_equip.copy()
plt.figure(figsize=(10,10))
sns.barplot(y= list_1['equip'], x= list_1['avg_equip'])
plt.title('AVERAGE OF EQUIPMENT LOST BY THE RUSSIAN ARMY PER DAY')
plt.xlabel('AVERAGE OF EQUIPMENT LOST')
plt.ylabel('EQUIPMENT')

#.set_index(the_most_lost_equip['equip']).stack().reset_index(level=1, drop = True)


# In[67]:


#Check ru_pers_losses
ru_pers_losses.info()


# In[68]:


#Change Date in Datetime type
ru_pers_losses['date'] = pd.to_datetime(ru_pers_losses['date'])
ru_pers_losses.info()


# In[69]:


#Merge 2 different DataFrames: russian_losses_equipment and russian_losses_personnel
equip_person = ru_equip_losses.merge(ru_pers_losses, left_on = ['day'], right_on = ['day'], how = 'left')
print(equip_person)


# In[70]:


equip_person.describe()


# In[71]:


#Replace NaN data with 0 equip_pers
equip_person.fillna(0, inplace = True)
equip_person.isnull()


# In[72]:


#Check how many Missing Values we have in the table:
equip_person.isnull().sum()


# In[73]:


#Check the max of personnel the russian army suffered since the beginning of the war by Ukrainian Governement & Russian Governement:
print('Total of people lost follow the Ukrainian Goverment figures:',  np.max(equip_person['personnel']))
print('Total of people lost follow the Russian Goverment figures:',  np.max(equip_person['POW - Provided by Russia']))


# In[74]:


#Graph related to Ukrainian Government figures on Casualties for the Russian Army
plt.figure(figsize=(15,7))
equip_person.groupby('personnel').mean()['day'].plot()
plt.xlabel('Casualties', labelpad=30)
plt.ylabel('Days')
plt.title('Casualties related to the Russian Army for the Ukrainian Government')
plt.show()


# In[75]:


#Graph related to Russian Government figures on Casualties
plt.figure(figsize=(15,7))
equip_person.groupby('POW - Provided by Russia').mean()['day'].plot.bar()
plt.xlabel('Casualties', labelpad=30)
plt.ylabel('Days')
plt.title('Casualties for the Russian Government')
plt.show()


# In[76]:


#Graph Comparison
plt.subplots(figsize=(15,10))

plt.plot(equip_person['day'],equip_person['personnel'])
plt.plot(equip_person['day'],equip_person['POW - Provided by Russia'])
plt.legend(['Ukrainian Governement', 'Russian Governement'])
plt.xlabel('Days')
plt.ylabel('Casualties')
plt.title('Casualties Comparison between Ukrainian Government vs Russian Government')


# In[ ]:





# In[ ]:




