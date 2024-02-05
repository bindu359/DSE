import pandas as pd
data={
    'Name':['John','Emma','Sam','Lisa','Tom'],
    'Age':[25,30,28,32,27],
    'Country':['USA','Canada','Australia','UK','Germany'],
    'Salary':[5000,60000,55000,70000,52000]
}
df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)

name_age=df[['Name','Age']]
print("Name and Age columns:")
print(name_age)

filtered_df=df[df['Country']=='USA']
print("\nFiltered Dataframe(Country=USA):")
print(filtered_df)

sorted_df=df.sort_values('Salary',ascending=False)
print("\n Sorted Dataframe(by salary in descending order):")
print(sorted_df)

average_salary=df['Salary'].mean()
print("\n Average salary:",average_salary)

df['Experience']=[3,6,4,8,5]
print("\n DataFrame with added experience column:")
print(df)

df.loc[df['Name']=='Emma','Salary']=65000
print("\n DataFrame after updating Emmma's salary:")
print(df)

df=df.drop('Experience',axis=1)
print("\n DataFrame after deleting Experience column:")
print(df)

# Original DataFrame:
#    Name  Age    Country  Salary
# 0  John   25        USA    5000
# 1  Emma   30     Canada   60000
# 2   Sam   28  Australia   55000
# 3  Lisa   32         UK   70000
# 4   Tom   27    Germany   52000
# Name and Age columns:
#    Name  Age
# 0  John   25
# 1  Emma   30
# 2   Sam   28
# 3  Lisa   32
# 4   Tom   27

# Filtered Dataframe(Country=USA):
#    Name  Age Country  Salary
# 0  John   25     USA    5000

#  Sorted Dataframe(by salary in descending order):
#    Name  Age    Country  Salary
# 3  Lisa   32         UK   70000
# 1  Emma   30     Canada   60000
# 2   Sam   28  Australia   55000
# 4   Tom   27    Germany   52000
# 0  John   25        USA    5000

#  Average salary: 48400.0

#  DataFrame with added experience column:
#    Name  Age    Country  Salary  Experience
# 0  John   25        USA    5000           3
# 1  Emma   30     Canada   60000           6
# 2   Sam   28  Australia   55000           4
# 3  Lisa   32         UK   70000           8
# 4   Tom   27    Germany   52000           5

#  DataFrame after updating Emmma's salary:
#    Name  Age    Country  Salary  Experience
# 0  John   25        USA    5000           3
# 1  Emma   30     Canada   65000           6
# 2   Sam   28  Australia   55000           4
# 3  Lisa   32         UK   70000           8
# 4   Tom   27    Germany   52000           5

#  DataFrame after deleting Experience column:
#    Name  Age    Country  Salary
# 0  John   25        USA    5000
# 1  Emma   30     Canada   65000
# 2   Sam   28  Australia   55000
# 3  Lisa   32         UK   70000
# 4   Tom   27    Germany   52000
# ​
