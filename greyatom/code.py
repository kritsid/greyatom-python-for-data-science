# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census = np.concatenate((new_record,data),axis=0)#add new_record as a new row in data
print(data.shape)
print(census.shape)
# ********************************************************
age = census[0]
max_age=age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)

# *********************************************************
race_0 = [i for i in census[2] if i==0]
race_0 = np.asarray(race_0)

race_1 = [i for i in census[2] if i==1]
race_1 = np.asarray(race_0)

race_2 = [i for i in census[2] if i==2]
race_2 = np.asarray(race_0)

race_3 = [i for i in census[2] if i==3]
race_3 = np.asarray(race_0)

race_4 = [i for i in census[2] if i==4]
race_4 = np.asarray(race_0)

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = min(len_0,len_1,len_2,len_3,len_4)

print(minority_race)

# /*********************************************************
# senior_citizens = [ for i in census[0] if i > 60]
senior_citizens = census[census[:,0]>60]
# print(senior_citizens)
working_hours_sum =  0
working_hours_sum = senior_citizens.sum(axis =0)[6]
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)
# *************************************************************
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
# print(type(high))
avg_pay_high = high.mean(axis =0)[7]

avg_pay_low = low.mean(axis =0)[7]



