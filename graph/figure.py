import pandas as pd
import random

# Legends

# Some sample data to plot.
cat_1 = ['y1', 'y2', 'y3', 'y4']
index_1 = range(0, 21, 1)
multi_iter1 = {'index': index_1}
for cat in cat_1:
    multi_iter1[cat] = [random.randint(10, 100) for x in index_1]

# Create a Pandas dataframe from the data.
index_2 = multi_iter1.pop('index')
df = pd.DataFrame(multi_iter1, index=index_2)
df = df.reindex(columns=sorted(df.columns))

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'data/Primary Sales · Secondary sales · All · Daily.csv'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)


#############################################################################
import pandas as pd
import pandas.io.data as web

# Some sample data to plot.
all_data = {}
for ticker in ['AAPL', 'GOOGL', 'IBM', 'YHOO', 'MSFT']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2012', '1/1/2013')

# Create a Pandas dataframe from the data.
df = pd.DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.items()})

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'legend_stock.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Adjust the width of the first column to make the date values clearer.
worksheet.set_column('A:A', 20)

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
max_row = len(df) + 1
for i in range(len(['AAPL', 'GOOGL'])):
    col = i + 1
    chart.add_series({
        'name':       ['Sheet1', 0, col],
        'categories': ['Sheet1', 2, 0, max_row, 0],
        'values':     ['Sheet1', 2, col, max_row, col],
        'line':       {'width': 1.00},
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Date', 'date_axis': True})
chart.set_y_axis({'name': 'Price', 'major_gridlines': {'visible': False}})

# Position the legend at the top of the chart.
chart.set_legend({'position': 'top'})

# Insert the chart into the worksheet.
worksheet.insert_chart('H2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
for i in range(len(cat_1)):
    col = i + 1
    chart.add_series({
        'name':       ['Sheet1', 0, col],
        'categories': ['Sheet1', 1, 0, 21, 0],
        'values':     ['Sheet1', 1, col, 21, col],
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Index'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})

# Insert the chart into the worksheet.
worksheet.insert_chart('G2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

# Lines

# Some sample data to plot.
list_data = [10, 20, 30, 20, 15, 30, 45]

# Create a Pandas dataframe from the data.
df = pd.DataFrame(list_data)

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'line.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.

chart.add_series({
    'categories': ['Sheet1', 1, 0, 7, 0],
    'values':     ['Sheet1', 1, 1, 7, 1],
})

# Configure the chart axes.
chart.set_x_axis({'name': 'Index', 'position_axis': 'on_tick'})
chart.set_y_axis({'name': 'Value', 'major_gridlines': {'visible': False}})

# Turn off chart legend. It is on by default in Excel.
chart.set_legend({'position': 'none'})

# Insert the chart into the worksheet.
worksheet.insert_chart('D2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

#############################################################################

import pandas as pd
import pandas.io.data as web

# Some sample data to plot.
all_data = {}
for ticker in ['AAPL', 'GOOGL', 'IBM', 'YHOO', 'MSFT']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2012', '1/1/2013')

# Create a Pandas dataframe from the data.
df = pd.DataFrame({tic: data['Adj Close']
                   for tic, data in all_data.items()})

# Create a Pandas Excel writer using XlsxWriter as the engine.
excel_file = 'legend_stock.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook = writer.book
worksheet = writer.sheets[sheet_name]

# Adjust the width of the first column to make the date values clearer.
worksheet.set_column('A:A', 20)

# Create a chart object.
chart = workbook.add_chart({'type': 'line'})

# Configure the series of the chart from the dataframe data.
max_row = len(df) + 1
for i in range(len(['AAPL', 'GOOGL'])):
    col = i + 1
    chart.add_series({
        'name':       ['Sheet1', 0, col],
        'categories': ['Sheet1', 2, 0, max_row, 0],
        'values':     ['Sheet1', 2, col, max_row, col],
        'line':       {'width': 1.00},
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Date', 'date_axis': True})
chart.set_y_axis({'name': 'Price', 'major_gridlines': {'visible': False}})

# Position the legend at the top of the chart.
chart.set_legend({'position': 'top'})

# Insert the chart into the worksheet.
worksheet.insert_chart('H2', chart)

# Close the Pandas Excel writer and output the Excel file.
writer.save()