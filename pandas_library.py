# -*- coding: utf-8 -*-
"""Pandas Library

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WgzakpkwYQ3GHL0te3R_LzwTaqzUaWvr

# Pandas

Pandas is used for data manipulation, analysis and cleaning. Python pandas is well suited for different kinds of data, such as:



*   Tabular data with heterogeneously-typed columns
*   Ordered and unordered time series data
*   Arbitrary matrix data with row & column labels
*   Unlabelled data
*   Any other form of observational or statistical data sets

**Python data structures**

1.   Series
2.   Data Frame

# Series

pandas.Series(data=None, index=None, dtype=None)

A Series is a one-dimensional labelled array-like object. It is capable of holding any data type, e.g. integers, floats, strings, Python objects, and so on. It can be seen as a data structure with two arrays: one functioning as the index, i.e. the labels, and the other one contains the actual data.
"""

import pandas as pd
data = pd.Series([11, 28, 37, 43, 25, 86])
print(data)

print()

#index and values
print(data.index)
print(data.values)

"""**Custom Indexes**"""

students=['Girish Attri','Neha Dhamija','Ravi Verma','Ankit Jain','Nikhil']
term1_marks=[43,35,65,45,49]

s=pd.Series(term1_marks, students)

print(s)

"""**Addition of two Series**"""

students=['Girish Attri','Neha Dhamija','Ravi Verma','Ankit Jain','Nikhil']
term1_marks=[43,35,65,45,49]
term2_marks=[42,49,43,40,42]

s1=pd.Series(term1_marks, students)
s2=pd.Series(term2_marks, students)

total=s1+s2

print(total)

students1=['Girish Attri','Neha Dhamija','Ravi Verma','Ankit Jain','Nikhil']
students2=['Nikhil', 'Rahul Sharma','Girish Attri', 'Ankit Jain']
term1_marks=[43,35,65,45,49]
term2_marks=[42,49,43,40]

s1=pd.Series(term1_marks, students1)
s2=pd.Series(term2_marks, students2)

total=s1+s2

print(s1, end='\n\n')
print(s2, end='\n\n')
print(total)

"""**Access values from a series**"""

students=['Girish Attri','Neha Dhamija','Ravi Verma','Ankit Jain','Nikhil']
term1_marks=[43,35,65,45,49]

s=pd.Series(term1_marks, students)

print(s['Girish Attri'])
print(s[ ['Girish Attri','Neha Dhamija','Ravi Verma' ] ])

"""**apply**

Series.apply(func, convert_dtype=True, args=(), **kwds)

The function "func" will be applied to the Series and it returns either a Series or a DataFrame, depending on "func".
"""

students=['Girish Attri','Neha Dhamija','Ravi Verma','Ankit Jain','Nikhil']
term1_marks=[43,35,65,45,49]

s=pd.Series(term1_marks, students)

s=s.apply(lambda x: x-5)
print(s)

pass_students=s.apply(lambda x: 'Pass' if x>33 else 'Fail')
print(pass_students)

#Filtering

students=['Girish Attri','Neha Dhamija','Ravi Verma','Ankit Jain','Nikhil']
term1_marks=[43,35,65,45,49]

s=pd.Series(term1_marks, students)

pass_students=s[s>50]
fail_students=s[s<50]

print(pass_students, end="\n\n")
print(fail_students, end="\n\n")

"""**Series from Dictionaries**"""

marks={
    "Girish Attri" : 84,
    "Ravi verma" : 74,
    "Pankaj Sharma" : 89,
    "Ankit Jain" : 84,
    "Nikhil Rastogi" : 89,
}

s=pd.Series(marks)

print(s)

"""**NaN (Not a Number)** 

Filtering and Filling Null Records
"""

marks={
    "Girish Attri" : 84,
    "Ravi verma" : 74,
    "Pankaj Sharma" : None,
    "Ankit Jain" : 84,
    "Nikhil Rastogi" : 89,
    "Sanjay Gupta" : None,
    "Neha Dhamija" : 84,
    "Shrishti Verma" : 90
}

s=pd.Series(marks)

print(s, end="\n\n")

#Filtering NaN
print(s.dropna(), end="\n\n")

#Filling NaN
print(s.fillna(0), end="\n\n")

#Filling Nan with astype
print(s.fillna(0).astype(int), end="\n\n")

"""# DataFrames

The underlying idea of a DataFrame is based on spreadsheets. We can see the data structure of a DataFrame as tabular and spreadsheet-like. A DataFrame logically corresponds to a "sheet" of an Excel document. A DataFrame has both a row and a column index.

Like a spreadsheet or Excel sheet, a DataFrame object contains an ordered collection of columns. Each column consists of a unique data typye, but different columns can have different types, e.g. the first column may consist of integers, while the second one consists of boolean values and so on.

There is a close connection between the DataFrames and the Series of Pandas. A DataFrame can be seen as a concatenation of Series, each Series having the same index, i.e. the index of the DataFrame.

**Creating DataFrames using Pandas Series**
"""

years = [2014, 2015, 2016, 2017]
shop1 = pd.Series([2409.14, 2941.01, 3496.83, 3119.55], index=years)
shop2 = pd.Series([1203.45, 3441.62, 3007.83, 3619.53], index=years)
shop3 = pd.Series([3412.12, 3491.16, 3457.19, 1963.10], index=years)

shops_df = pd.concat( [shop1, shop2, shop3] )           #Column Wise Concatenation
print(shops_df, end="\n\n")

shops_df = pd.concat( [shop1,shop2,shop3], axis=1)
print(shops_df, end="\n\n")

"""**Column Names**"""

years = [2014, 2015, 2016, 2017]
shop1 = pd.Series([2409.14, 2941.01, 3496.83, 3119.55], index=years)
shop2 = pd.Series([1203.45, 3441.62, 3007.83, 3619.53], index=years)
shop3 = pd.Series([3412.12, 3491.16, 3457.19, 1963.10], index=years)

shops_df = pd.concat( [shop1,shop2,shop3], axis=1)

col_names = ['Shop 1', 'Shop 2', 'Shop 3']
shops_df.columns = col_names

print(shops_df, end="\n\n")

"""**Dataframes from Dictionaries**"""

cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania", 
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"],
          
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          }
city_frame = pd.DataFrame(cities)
city_frame

"""**Custom Indexing**"""

indexes = list(map(lambda x : "City " + str(x), list(range(1,len(city_frame)+1))))

city_frame = pd.DataFrame(cities, index=indexes)
city_frame

"""**Using Existing Column as Index**"""

city_frame=city_frame.set_index('country')
print(city_frame)

"""**Label Indexing on the Rows**"""

#print(city_frame['Germany'])        #Error

print(city_frame.loc['Germany'], end="\n\n")

print(city_frame.loc[["Germany", "France"]], end="\n\n")

print(city_frame.loc[city_frame.population>2000000])

"""**Accessing the columns of a DataFrame**"""

print(city_frame["population"])       #as dictionary like way

#or

print(city_frame.population)          #as attribute

"""**Adding New Columns to DataFrames**"""

area = [1572, 891.85, 605.77, 1285, 
        105.4, 414.6, 228, 755, 
        525.2, 517, 101.9, 310.4, 
        181.8]
# area could have been designed as a list, a Series, an array or a scalar   
city_frame["area"] = area
print(city_frame)

"""**Sorting DataFrames**"""

city_frame = city_frame.sort_values(by="area", ascending=False)
print(city_frame)

"""**Data Frames from Nested Dictionaries**"""

growth = {"Switzerland": {"2010": 3.0, "2011": 1.8, "2012": 1.1, "2013": 1.9},
          "Germany": {"2010": 4.1, "2011": 3.6, "2012":	0.4, "2013": 0.1},
          "France": {"2010":2.0,  "2011":2.1, "2012": 0.3, "2013": 0.3},
          "Greece": {"2010":-5.4, "2011":-8.9, "2012":-6.6, "2013":	-3.3},
          "Italy": {"2010":1.7, "2011":	0.6, "2012":-2.3, "2013":-1.9}
          }

growth_frame = pd.DataFrame(growth)
print(growth_frame, end="\n\n")

print(growth_frame.T)

"""# Reading and Writing data in Files 

Pandas supported file formats:

1.  Delimiter-separated files, like e.g. csv
2.  Microsoft Excel files
3.  HTML
4.  XML
5.  JSON

**Reading and Writing data from/to a csv file.**
"""

import pandas as pd
cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          
          "country": ["England", "Germany", "Spain", "Italy",
                      "France", "Austria", "Romania", 
                      "Germany", "Hungary", "Poland", "Spain",
                      "Germany", "Italy"],
          
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          }

city_frame = pd.DataFrame(cities, columns=["name", "population"], index=cities["country"])
print(city_frame)

#Saving Data to CSV File
city_frame.to_csv("countries_population.csv", sep=";")


#Reading Data from CSV File
city_frame = pd.read_csv("countries_population.csv", sep=";", index_col=0)


print(city_frame)

"""# Data Visualization using Pandas

**Line plots**
"""

#Line Plots using Series

#data = [100, 120, 140, 180, 200, 210, 214]
#s = pd.Series(data, index=range(1,len(data)+1))

index=['Jan','Feb','Mar','Apr','May','Jun']
data1=[4456,4576,7656,7654,6754,6587]
data2=[4566,7645,6565,7645,5456,5677]

s1=pd.Series(data1,index)
s2=pd.Series(data2,index)

df=pd.concat( [s1,s2], axis=1 )

print(df)
df.plot.pie(figsize=(6,6), subplots=True)

#Line Plots using DataFrames

fruits = ['A', 'B', 'C', 'D']
quantities = [20, 33, 52, 10]
s = pd.Series(quantities, index=fruits)

print(s)
s.plot(use_index=True)

cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "area" : [1572, 891.85, 605.77, 1285, 
                    105.4, 414.6, 228, 755, 
                    525.2, 517, 101.9, 310.4, 
                    181.8]
}
city_frame = pd.DataFrame(cities,
                          columns=["population", "area"],
                          index=cities["name"])

city_frame['area'] *= 1000

city_frame.plot()

"""**Bar Plots**"""

#Bar Plots from Series

data = [100, 120, 140, 180, 200, 210, 214]
s = pd.Series(data, index=range(len(data)))
s.plot(kind="bar")

#Bar Plot using DataFrames

cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "area" : [1572, 891.85, 605.77, 1285, 
                    105.4, 414.6, 228, 755, 
                    525.2, 517, 101.9, 310.4, 
                    181.8]
}
city_frame = pd.DataFrame(cities,
                          columns=["population", "area"],
                          index=cities["name"])

city_frame['area'] *= 1000

city_frame.plot(kind="bar")

"""**Pie Chart**"""

#Pie Chart using Series

fruits = ['apples', 'pears', 'cherries', 'bananas']
series = pd.Series([20, 30, 40, 10], 
                   index=fruits, 
                   name='series')
series.plot.pie(figsize=(6, 6))

cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                   "Paris", "Vienna", "Bucharest", "Hamburg", 
                   "Budapest", "Warsaw", "Barcelona", 
                   "Munich", "Milan"],
          "population": [8615246, 3562166, 3165235, 2874038,
                         2273305, 1805681, 1803425, 1760433,
                         1754000, 1740119, 1602386, 1493900,
                         1350680],
          "area" : [1572, 891.85, 605.77, 1285, 
                    105.4, 414.6, 228, 755, 
                    525.2, 517, 101.9, 310.4, 
                    181.8]
}
city_frame = pd.DataFrame(cities,
                          columns=["population", "area"],
                          index=cities["name"])

city_frame['area'] *= 1000

city_frame.plot.pie(figsize=(6,6), subplots=True, legend=False)