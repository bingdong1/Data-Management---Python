
# coding: utf-8

# PRED 420
# Assigment #1
# Dong Bing

# In[ ]:

#Import the necessary package

import pandas as pd
import numpy as np


# In[ ]:

#set to data frame
survey2014_df = pd.read_csv('sfo_survey2014.csv')

#Check the dimention
#survey2014_df.shape
#(2818, 95)

#Checking for missing values
#survey2014_df.isnull().sum()


# In[ ]:

#set to data frame
survey2015_df = pd.read_csv('sfo_survey2015.csv')

#Check the dimention
#survey2015_df.shape
#(2958, 90)

#Checking for missing values
#survey2015_df.isnull().sum()


# In[ ]:

#set to data frame
survey2016_df = pd.read_csv('sfo_survey2016.csv')

#Check the dimention
#survey2016_df.shape
#(3087, 97)

#Checking for missing values
#survey2015_df.isnull().sum()


# Part 1
# 
# Create a single summary data set of ratings data using the data from all three years. Your new data set should include all rating scale response data (e.g. "Rating SFO" responses, "Cleanliness of SFO" responses, safetiness item responses, getting to the airport items, and so on; see below), unique respondent IDs, residence location (Q16LIVE in the 2016 data).
# 
# 
# (a) List the the variables from each year that you used to create this data set using the original names they had in the data set they appeared in.
# 
# (b) Document any variable name changes so that it's clear what the original variables are whose names you changed. (Otherwise, a user of your data wouldn't be able to know what these variables are, or how to use them.)
# 
# 2014
# 'RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU','Q16LIVE'
# 
# **Note for 2014, We create the "Year" variable and set its value to 2014.
# 
# 2015
# 'RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU'
# 
# **Note for 2015, the variable 'Q12PRECHECKRATE' is not in the original dataset, so we had to create a new variable under this name and set its value to nan. In addtion we create the "Year" variable and set its value to 2015.
# 
# 2016
# 'RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU'
# 
# **Note for 2016, we have to rename the variable '*RESPNUM' to 'RESPNUM' in order to match the previous 2 years, In addtion we create the "Year" variable and set its value to 2016.
# 

# In[ ]:

#Check out first 5 rows of the data for 2014
survey2014_df.head(5)


# In[ ]:

#Select the rating variable for 2014
survey2014_df_rate = survey2014_df[['RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU','Q16LIVE']] 


# In[ ]:

#Add the year variable for 2014
survey2014_df_rate_YEAR = survey2014_df_rate.assign(YEAR = 2014)


# In[ ]:

#Check the new rating dataset for 2014

#survey2014_df_rate_YEAR.head(5)

#survey2014_df_rate_YEAR.shape

#survey2014_df_rate_YEAR.isnull().sum()


# In[ ]:

#Check out first 5 rows of the data for 2015
#survey2015_df.head(5)

#Select the rating variable for 2015
#survey2015_df_rate = survey2015_df[['RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU']]
#NameError: name 'Q12PRECHECKRATE' is not defined

#Add missing column and assign NAN value for 2015
survey2015_df = survey2015_df.assign(Q12PRECHECKRATE=np.nan)

#Combind rate data with missing column for 2015
survey2015_df_rate = survey2015_df[['RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU','Q16LIVE']]


# In[ ]:

#Add the year variable for 2015
survey2015_df_rate_YEAR = survey2015_df_rate.assign(YEAR = 2015)

#Check the new rating dataset for 2015
survey2015_df_rate_YEAR.head(5)


# In[ ]:

#Check out first 5 rows of the data for 2016
#survey2016_df.head(5)

#Combind rate data with missing column for 2016
#survey2016_df_rate = survey2016_df[['RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU']]

#KeyError: "['RESPNUM'] not in index", need to rename the column

# rename "*RESPNUM" to "RESPNUM" for 2016
survey2016_df=survey2016_df.rename(columns={'*RESPNUM':'RESPNUM'}) 

#Combind rate data with renamed column for 2016
survey2016_df_rate = survey2016_df[['RESPNUM','Q7ART','Q7FOOD','Q7STORE','Q7SIGN','Q7WALKWAYS','Q7SCREENS','Q7INFODOWN','Q7INFOUP','Q7WIFI','Q7ROADS','Q7PARK','Q7AIRTRAIN','Q7LTPARKING','Q7RENTAL','Q7ALL','Q9BOARDING','Q9AIRTRAIN','Q9RENTAL','Q9FOOD','Q9RESTROOM','Q9ALL','Q10SAFE','Q12PRECHECKRATE','Q13GETRATE','Q14FIND','Q14PASSTHRU','Q16LIVE']]


# In[ ]:

#Add the year variable for 2016
survey2016_df_rate_YEAR = survey2016_df_rate.assign(YEAR = 2016)

#Check the new rating dataset for 2016
survey2016_df_rate_YEAR.head(5)


# In[ ]:

#Concat all 3 rate data together

con_df = pd.concat([survey2014_df_rate_YEAR ,survey2015_df_rate_YEAR,survey2016_df_rate_YEAR])

#con_df 


# In[ ]:

#What type of data is it

type(con_df)


# In[ ]:

#size

con_df.shape


# In[ ]:

# You can do something like this in Part 1 when asked to fined missing values.
con_df.isnull().sum()


# (c) Describe this data set you created in terms of its size, the variables in it, and how the variables are coded. How many missing values do you have on the ratings variables?
# 
# This data set have 8863 rows and 29 columns, below are the variables in this dataset. There are 6884 missing values for the variable "Q12PRECHECKRATE". 
# 
# Variable Name      Missing
# RESPNUM               0
# Q7ART                 0
# Q7FOOD                0
# Q7STORE               0
# Q7SIGN                0
# Q7WALKWAYS            0
# Q7SCREENS             0
# Q7INFODOWN            0
# Q7INFOUP              0
# Q7WIFI                0
# Q7ROADS               0
# Q7PARK                0
# Q7AIRTRAIN            0
# Q7LTPARKING           0
# Q7RENTAL              0
# Q7ALL                 0
# Q9BOARDING            0
# Q9AIRTRAIN            0
# Q9RENTAL              0
# Q9FOOD                0
# Q9RESTROOM            0
# Q9ALL                 0
# Q10SAFE               0
# Q12PRECHECKRATE    6884
# Q13GETRATE            0
# Q14FIND               0
# Q14PASSTHRU           0
# Q16LIVE               0
# YEAR                  0
# dtype: int64
# 
# 

# In[ ]:

(D) Write your new data set to a csv file with an initial header record that includes the variable names.


# In[ ]:

# Save the combined rating for 2014-2016 to CSV file
con_df.to_csv("Combined_Rating_df.csv")


# Part 2: Identify the top three (3) comments made by gender of respondent in survey years 2015 and 2016. Report the top three (3) most common comments based on their relative frequency for each gender category. Include each of the comments' text that's indicated in the data dictionary documents. For each comment, indicate its relative frequency.

# In[ ]:

#Create data frame for male and female

male_users_2015_df=survey2015_df[survey2015_df.Q19GENDER==1]   

female_users_2015_df=survey2015_df[survey2015_df.Q19GENDER==2] 


# In[ ]:

#Check Data

male_users_2015_df.head(5)

female_users_2015_df.head(5)


# In[ ]:

#Need to convert the value for female and male from 2016 to 2 and 1 to match 2015
#survey2016_df.loc[survey2016_df.Q20GENDER == 'Female', 2]
#survey2016_df.loc[survey2016_df.Q20GENDER == 'Male', 1]

survey2016_df.replace(to_replace=dict(Female=2, Male=1), inplace=True)


# In[ ]:

#Create data frame for male and female
male_users_2016_df=survey2016_df[survey2016_df.Q20GENDER==1]   
female_users_2016_df=survey2016_df[survey2016_df.Q20GENDER==2] 


# In[ ]:

#Check Data
male_users_2016_df.head(5)


# In[ ]:

#Identify the top three (3) comments made by male in survey years 2015

male_users_2015_df_COM = male_users_2015_df[['Q8COM1','Q8COM2','Q8COM3']]


#male_users_2015_df_COM.stack().value_counts().head(3) 


# In[ ]:

#Code the comments text according to data dictionary for male in 2015

male_users_2015_df_COM['Q8COM1'] = male_users_2015_df_COM['Q8COM1'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2015_df_COM['Q8COM1'] = male_users_2015_df_COM['Q8COM1'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
male_users_2015_df_COM['Q8COM1'] = male_users_2015_df_COM['Q8COM1'].replace([505.0], 'Add plugs/electrical outlets/places to charge devices')
male_users_2015_df_COM['Q8COM2'] = male_users_2015_df_COM['Q8COM2'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2015_df_COM['Q8COM2'] = male_users_2015_df_COM['Q8COM2'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
male_users_2015_df_COM['Q8COM2'] = male_users_2015_df_COM['Q8COM2'].replace([505.0], 'Add plugs/electrical outlets/places to charge devices')
male_users_2015_df_COM['Q8COM3'] = male_users_2015_df_COM['Q8COM3'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2015_df_COM['Q8COM3'] = male_users_2015_df_COM['Q8COM3'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
male_users_2015_df_COM['Q8COM3'] = male_users_2015_df_COM['Q8COM3'].replace([505.0], 'Add plugs/electrical outlets/places to charge devices')


# In[ ]:

#frequency for male in 2015
male_users_2015_df_COM.stack().value_counts().head(3) 

#relative frequency for male in 2015
male_users_2015_df_COM.stack().value_counts(normalize=True).head(3)  


# Frequency for male in 2015
# 
# Good experience/keep up the good work/other positive comment          84
# Need more places to eat/drink/more variety in types of restaurants    60
# Add plugs/electrical outlets/places to charge devices                 31
# dtype: int64
# 
# Relative Frequency for male in 2015
# 
# Good experience/keep up the good work/other positive comment          0.109518
# Need more places to eat/drink/more variety in types of restaurants    0.078227
# Add plugs/electrical outlets/places to charge devices                 0.040417
# dtype: float64

# In[ ]:

#Identify the top three (3) comments made by female in survey years 2015

female_users_2015_df_COM = female_users_2015_df[['Q8COM1','Q8COM2','Q8COM3']]

#female_users_2015_df_COM.stack().value_counts().head(3) 


# In[ ]:

#Code the comments text according to data dictionary for female in 2015

female_users_2015_df_COM['Q8COM1'] = female_users_2015_df_COM['Q8COM1'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2015_df_COM['Q8COM1'] = female_users_2015_df_COM['Q8COM1'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
female_users_2015_df_COM['Q8COM1'] = female_users_2015_df_COM['Q8COM1'].replace([505.0], 'Add plugs/electrical outlets/places to charge devices')
female_users_2015_df_COM['Q8COM2'] = female_users_2015_df_COM['Q8COM2'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2015_df_COM['Q8COM2'] = female_users_2015_df_COM['Q8COM2'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
female_users_2015_df_COM['Q8COM2'] = female_users_2015_df_COM['Q8COM2'].replace([505.0], 'Add plugs/electrical outlets/places to charge devices')
female_users_2015_df_COM['Q8COM3'] = female_users_2015_df_COM['Q8COM3'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2015_df_COM['Q8COM3'] = female_users_2015_df_COM['Q8COM3'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
female_users_2015_df_COM['Q8COM3'] = female_users_2015_df_COM['Q8COM3'].replace([505.0], 'Add plugs/electrical outlets/places to charge devices')


# In[ ]:

#frequency for female in 2015

female_users_2015_df_COM.stack().value_counts().head(3) 

#relative frequency for female in 2015

female_users_2015_df_COM.stack().value_counts(normalize=True).head(3)  


# In[ ]:

Frequency for male in 2015

Good experience/keep up the good work/other positive comment          95
Need more places to eat/drink/more variety in types of restaurants    77
Add plugs/electrical outlets/places to charge devices                 40
dtype: int64

Relative Frequency for male in 2015

Good experience/keep up the good work/other positive comment          0.102703
Need more places to eat/drink/more variety in types of restaurants    0.083243
Add plugs/electrical outlets/places to charge devices                 0.043243
dtype: float64    


# In[ ]:

#Identify the top three (3) comments made by female in survey years 2016

male_users_2016_df_COM = male_users_2016_df[['Q8COM','Q8COM2','Q8COM3','Q8COM4','Q8COM5']]
female_users_2016_df_COM = female_users_2016_df[['Q8COM','Q8COM2','Q8COM3','Q8COM4','Q8COM5']]


# In[ ]:

#male_users_2016_df_COM.stack().value_counts().head(3) 
#female_users_2016_df_COM.stack().value_counts().head(3) 


# In[ ]:

#Code the comments text according to data dictionary for male in 2016

male_users_2016_df_COM['Q8COM'] = male_users_2016_df_COM['Q8COM'].replace([0.0], 'Blank/No Response')
male_users_2016_df_COM['Q8COM'] = male_users_2016_df_COM['Q8COM'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2016_df_COM['Q8COM'] = male_users_2016_df_COM['Q8COM'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
male_users_2016_df_COM['Q8COM2'] = male_users_2016_df_COM['Q8COM2'].replace([0.0], 'Blank/No Response')
male_users_2016_df_COM['Q8COM2'] = male_users_2016_df_COM['Q8COM2'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2016_df_COM['Q8COM2'] = male_users_2016_df_COM['Q8COM2'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
male_users_2016_df_COM['Q8COM3'] = male_users_2016_df_COM['Q8COM3'].replace([0.0], 'Blank/No Response')
male_users_2016_df_COM['Q8COM3'] = male_users_2016_df_COM['Q8COM3'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2016_df_COM['Q8COM3'] = male_users_2016_df_COM['Q8COM3'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
male_users_2016_df_COM['Q8COM4'] = male_users_2016_df_COM['Q8COM4'].replace([0.0], 'Blank/No Response')
male_users_2016_df_COM['Q8COM4'] = male_users_2016_df_COM['Q8COM4'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2016_df_COM['Q8COM4'] = male_users_2016_df_COM['Q8COM4'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
male_users_2016_df_COM['Q8COM5'] = male_users_2016_df_COM['Q8COM5'].replace([0.0], 'Blank/No Response')
male_users_2016_df_COM['Q8COM5'] = male_users_2016_df_COM['Q8COM5'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
male_users_2016_df_COM['Q8COM5'] = male_users_2016_df_COM['Q8COM5'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')


# In[ ]:

#frequency for male in 2016
male_users_2016_df_COM.stack().value_counts().head(3) 

#relaative frequency for male in 2016
male_users_2016_df_COM.stack().value_counts(normalize=True).head(3)  


# In[ ]:

Frequency for male in 2016

Blank/No Response                                                     686
Good experience/keep up the good work/other positive comment           94
Need more places to eat/drink/more variety in types of restaurants     89
dtype: int64

Relative Frequency for male in 2016

Blank/No Response                                                     0.392449
Good experience/keep up the good work/other positive comment          0.053776
Need more places to eat/drink/more variety in types of restaurants    0.050915
dtype: float64


# In[ ]:

#Code the comments text according to data dictionary for female in 2016

female_users_2016_df_COM['Q8COM'] = female_users_2016_df_COM['Q8COM'].replace([0.0], 'Blank/No Response')
female_users_2016_df_COM['Q8COM'] = female_users_2016_df_COM['Q8COM'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2016_df_COM['Q8COM'] = female_users_2016_df_COM['Q8COM'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
female_users_2016_df_COM['Q8COM2'] = female_users_2016_df_COM['Q8COM2'].replace([0.0], 'Blank/No Response')
female_users_2016_df_COM['Q8COM2'] = female_users_2016_df_COM['Q8COM2'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2016_df_COM['Q8COM2'] = female_users_2016_df_COM['Q8COM2'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
female_users_2016_df_COM['Q8COM3'] = female_users_2016_df_COM['Q8COM3'].replace([0.0], 'Blank/No Response')
female_users_2016_df_COM['Q8COM3'] = female_users_2016_df_COM['Q8COM3'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2016_df_COM['Q8COM3'] = female_users_2016_df_COM['Q8COM3'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
female_users_2016_df_COM['Q8COM4'] = female_users_2016_df_COM['Q8COM4'].replace([0.0], 'Blank/No Response')
female_users_2016_df_COM['Q8COM4'] = female_users_2016_df_COM['Q8COM4'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2016_df_COM['Q8COM4'] = female_users_2016_df_COM['Q8COM4'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')
female_users_2016_df_COM['Q8COM5'] = female_users_2016_df_COM['Q8COM5'].replace([0.0], 'Blank/No Response')
female_users_2016_df_COM['Q8COM5'] = female_users_2016_df_COM['Q8COM5'].replace([999.0], 'Good experience/keep up the good work/other positive comment')
female_users_2016_df_COM['Q8COM5'] = female_users_2016_df_COM['Q8COM5'].replace([202.0], 'Need more places to eat/drink/more variety in types of restaurants')


# In[ ]:

#frequency for female in 2016
female_users_2016_df_COM.stack().value_counts().head(3) 

#relaative frequency for male in 2016
female_users_2016_df_COM.stack().value_counts(normalize=True).head(3)  


# In[ ]:

Frequency for female in 2016

Blank/No Response                                                     682
Need more places to eat/drink/more variety in types of restaurants     94
Good experience/keep up the good work/other positive comment           92
dtype: int64


Relative Frequency for female in 2016

Blank/No Response                                                     0.385965
Need more places to eat/drink/more variety in types of restaurants    0.053198
Good experience/keep up the good work/other positive comment          0.052066
dtype: float64


# Part 3: Using the data you created in 1, summarize the distribution of the SFO Airport "as a whole" ratings by respondent residence location category and report your results. These are ratings about the airport, overall. For example, in the 2016 data, the variable is called Q7ALL. Make sure how you do this takes into account the nature of the data for this variable.

# In[ ]:

#check the data from part 1
con_df.head(5)


# In[ ]:

#Distribution of the SFO Airport "as a whole" ratings by respondent residence loacation category

con_df.groupby(["Q9ALL","Q16LIVE"]).size()


# Distribution of the SFO Airport "as a whole" ratings by respondent residence loacation category
# 
# Q9ALL  Q16LIVE
# 0      0            27
#        1            51
#        2             6
#        3           109
# 1      1            10
#        3             6
# 2      0             4
#        1            28
#        3            69
# 3      0            41
#        1           404
#        2            58
#        3           796
#        4             2
# 4      0           134
#        1          1272
#        2           180
#        3          2247
#        4             2
# 5      0           109
#        1          1096
#        2           172
#        3          1971
# 6      0            10
#        1            15
#        2             4
#        3            40
# dtype: int64

# Part 4: Profile respondents for follow-up participation in qualitative research by creating a data set that describes them. Further investigation of some of the issues apparent in the survey data is going to be pursued by inviting selected respondents to participate in follow-up research. The file select_resps.csv identifies the respondents to be targeted. These respondents were surveyed in either 2015 or 2016.

# In[ ]:

#Create Data Frame for 2015 and 2016 only

con_df_2015_2016 = con_df.loc[con_df['YEAR'].isin(['2015','2016'])]

#Check Data Frame Dimentions
#con_df_2015_2016.shape


# In[ ]:

#Load Select Respondents List

select_resps_df = pd.read_csv('select_resps.csv')


# In[ ]:

#Separate the Select Respondents List to 2015 and 2016

select_resps_df_2015=select_resps_df[select_resps_df.year==2015]   
select_resps_df_2016=select_resps_df[select_resps_df.year==2016] 


# In[ ]:

#Extract 2015 data according to selection sheet
con_df_2015 = con_df_2015_2016[(con_df_2015_2016.RESPNUM.isin(select_resps_df_2015.RESPNUM)) & (con_df_2015_2016.YEAR.isin(select_resps_df_2015.year))]


# In[ ]:

#Extract 2016 data according to selection sheet
con_df_2016 = con_df_2015_2016[(con_df_2015_2016.RESPNUM.isin(select_resps_df_2016.RESPNUM)) & (con_df_2015_2016.YEAR.isin(select_resps_df_2016.year))]


# In[ ]:

#Extract Respondent Number from original 2015 dataset
survey2015_df_select = survey2015_df[(survey2015_df.RESPNUM.isin(con_df_2015.RESPNUM))]

#Create 2015 Demographic and Travel Behavior Data Frame
survey2015_df_select = survey2015_df_select[['RESPNUM','INTDATE','DESTGEO','DESTMARK','Q2PURP1','Q2PURP2','Q2PURP3','Q3PARK','Q4BAGS','Q4STORE','Q4FOOD','Q7WIFI','Q5TIMESFLOWN','Q5FIRSTTIME','Q6LONGUSE','Q16LIVE','Q18AGE','Q19GENDER','Q20INCOME','Q21FLY','Q22SJC','Q22OAK','LANG']]

#Add the Variable "Year" to the 2015 Data Frame
survey2015_df_select_YEAR = survey2015_df_select.assign(YEAR = 2015)


# In[ ]:

#Check Data Frame for 2016 for difference
#survey2016_df.head(5)

#Rename the Respondent Number Variable so it match to 2015
survey2016_df=survey2016_df.rename(columns={'*RESPNUM':'RESPNUM}) 

#Extract Respondent Number from original 2016 dataset
survey2016_df_select = survey2016_df[(survey2016_df.RESPNUM.isin(con_df_2016.RESPNUM))]

#Create 2016 Demographic and Travel Behavior Data Frame
survey2016_df_select = survey2016_df_select[['RESPNUM','INTDATE','DESTGEO','DESTMARK','Q2PURP1','Q2PURP2','Q2PURP3','Q3PARK','Q4BAGS','Q4STORE','Q4FOOD','Q7WIFI','Q5TIMESFLOWN','Q5FIRSTTIME','Q6LONGUSE','Q16LIVE','Q19AGE','Q20GENDER','Q21INCME','Q22FLY','Q23SJC','Q23OAK','LANG']]

#Add the Variable "Year" to the 2016 Data Frame
survey2016_df_select_YEAR = survey2016_df_select.assign(YEAR = 2016)


# In[ ]:

#The INDATE variable for both data frame have different type of values, convert the 2016 value to 2015 format

#Substring the INDATE Variable for 2016
survey2016_df_select_YEAR.INTDATE = survey2016_df_select_YEAR.INTDATE.str[2:4]

#Remove the "/" after the substring function
survey2016_df_select_YEAR.INTDATE = survey2016_df_select_YEAR.INTDATE.replace({'/': ''}, regex=True)


# In[ ]:

#Verify the newly format 2016 INDATE matches up to 2015
#survey2016_df_select_YEAR.head(5)


# In[ ]:

#The Age Tier values between two data frame are also inconsistent
#Replace value for Age tier for 2015 so it matches to 2016

survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([1], 'Under 18')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([2], '18 - 24')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([3], '25 - 34')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([4], '35 - 44')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([5], '45 - 54')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([6], '55 - 64')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([7], '65 and over')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([8], 'Dont Know/Refused')
survey2015_df_select_YEAR['Q18AGE'] = survey2015_df_select_YEAR['Q18AGE'].replace([0], 'Blank/Multiple responses')


# In[ ]:

#Replace value for 2016 Age tier in "Don't know or Refused" to "Dont know/Refused" so it match 2015

survey2016_df_select_YEAR['Q19AGE'] = survey2016_df_select_YEAR['Q19AGE'].replace("Don't Know or Refused", 'Dont Know/Refused')


# In[ ]:

#Rename all 2015 colum so they match up to 2016

survey2015_df_select_YEAR=survey2015_df_select_YEAR.rename(columns={'Q18AGE':'Q19AGE'}) 
survey2015_df_select_YEAR=survey2015_df_select_YEAR.rename(columns={'Q19GENDER':'Q20GENDER'})
survey2015_df_select_YEAR=survey2015_df_select_YEAR.rename(columns={'Q20INCOME':'Q21INCME'})
survey2015_df_select_YEAR=survey2015_df_select_YEAR.rename(columns={'Q21FLY':'Q22FLY'})
survey2015_df_select_YEAR=survey2015_df_select_YEAR.rename(columns={'Q22SJC':'Q23SJC'})
survey2015_df_select_YEAR=survey2015_df_select_YEAR.rename(columns={'Q22OAK':'Q23OAK'})


# In[ ]:

#Combine the two dataset for 2015 and 2016

con_df_select = pd.concat([survey2015_df_select_YEAR ,survey2016_df_select_YEAR])


# In[ ]:

#Check the final combined dataset
con_df_select.head(5)


# In[ ]:

#Save the final Dataset to CSV
con_df_select.to_csv("con_df_select.csv")


# In[ ]:

con_df_select.shape


# In[ ]:

#find frequency for parking

con_df_select.Q3PARK.value_counts()


# Frequency for Parking
# 
# 3.0    5
# 4.0    4
# 1.0    4
# 4      3
# 3      2
# 1      1
# 2      1
# 2.0    1
# 0.0    1
# Name: Q3PARK, dtype: int64

# In[ ]:

#find frequency for time flown

con_df_select.Q5TIMESFLOWN.value_counts()


# Frequency for Time Flowwn
# 
# 3    76
# 1    33
# 2    31
# 4    20
# 6    13
# 5     7
# Name: Q5TIMESFLOWN, dtype: int64

# In[ ]:

#find frequency for how long fly SFO

con_df_select.Q6LONGUSE.value_counts()


# Frequency for how long fly SFO
# 
# 4    93
# 2    46
# 3    22
# 1    18
# 0     1
# Name: Q6LONGUSE, dtype: int64

# Part 5

# In[ ]:

#Save in pickle file
import pickle
con_df.to_pickle("Combined_Rating_df.pkl")
con_df_select.to_pickle("Select_Demographic_df.pkl")


# In[ ]:

#unpickle
df = pd.read_pickle("Combined_Rating_df.pkl")
df.head()

df = pd.read_pickle("Select_Demographic_df.pkl")
df.head()


# 
