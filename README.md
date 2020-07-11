# Surf and Treats!
![Pitch](images/2020/07/pitch.png)

#### This repo demonstrate some techniques using SQL, SQLAlchemy, Flask, Python, Pandas, statistical analysis, and ploting to present an analysis pitch for a surf and ice cream store in Hawaii.  


- `hawaii.sqlite` - data source file
- `climate_analysis.ipynb` - Jupyter notebook notes
- `app.py` - Python code with routes for Flask showing sqlite file data
- `surfs_challenge.ipynb` - Jupyter notebook of python code showing the final
analysis

# Analysis
After previous rounds of data gathering and presentation, I am following up on
data requested for seasonality and viability of the surf and ice cream shop.
Below is the data we've found by looking at all the June and December months
precipitation across our entire data set (2010-01-01 to 2017-08-23).  From the analysis of the data, we can see that in June, we average .13 inches of rain.  And in December, we average .22 inches of rain.  It is clear that there are seasonal differences of rainfall between months.  To put in perspective, .1" and .25" of rain are defined by rain insurance agencies as categories next to each other.  (Source:https://www.usweatherinsurance.com/rain-insurance/).  We also know that the max rainfall between seasons are about 2 inches, which is significant.  Finally, 3rd quartile stats of both months show similarity of .12 and .15 inches.  This tells us, most rainfall amount in June is similar to December.  

References:

June

|        | precipitation
|--------|---------------
| count  |  1574.000000
| mean   |     0.136360
| std    |     0.335731
| min    |     0.000000
| 25%    |     0.000000
| 50%    |     0.020000
| 75%    |     0.120000
| max    |     4.430000

December

|        | precipitation
|--------|---------------
|count   | 1405.000000
|mean    |    0.216819
|std     |    0.541399
|min     |    0.000000
|25%     |    0.000000
|50%     |    0.030000
|75%     |    0.150000
|max     |    6.420000

![June and December Precipitation](images/2020/07/june-and-december-precipitation.png)

# Limitation of Analysis and Recommendation
- With the data and analysis at hand we do not know when are rains occurring, if it is during the day or at night
- We also do not know how frequent rain is occurring on a month by month basis
- We also had not examined the severity of the rain.  

I recommend we obtain further data on hours of rain occurrence, then filter and understand rain pattern during business hours.  Additionally, with the existing data set, we can start on examining how many consecutive rainy days break down month by month.  The result may help decide if certain months the business should simply close and let us take a break or vacation.  Lastly, we should examine all the months and its outliers in rainfall, as these can be indicative of severe weather events.   
