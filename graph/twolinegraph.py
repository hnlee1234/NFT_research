import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/content/test.csv', usecols=[1,2])
data.plot()
plt.show()