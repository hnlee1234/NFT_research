import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = pd.read_csv('/data/date_primary_secondary.csv',parse_dates=['DateTime'], dayfirst=False, infer_datetime_format=True)
data.set_index('DateTime', inplace=True)
data.index = pd.to_datetime(data.index)
data.plot()
#data['datetime'] = pd.to_datetime(data['datetime'])
#myFmt = mdates.DateFormatter('%Y-%m-%d')
#plt.gca().xaxis.set_major_formatter(myFmt)
plt.title('Primary sales and Secondary sales comparison',fontsize = 'large')
plt.ylabel('Sales',fontsize = 'medium')
plt.xlabel('Year',fontsize = 'medium')
plt.show()