import numpy as np
import pandas as pd

#arr = np.array([10, 20, 30, 40, 50])
#print("Array:", arr)
#print("Mean:", np.mean(arr))

#data = {
#    "Name": ["Yoges", "Arun", "Kumar"],
#    "Marks": [85, 90, 78]
#}

#df = pd.DataFrame(data)
#print("\nStudent Data:")
#print(df)

#print("\nAverage Marks:", df["Marks"].mean())

## 2 example task
np.random.seed(0)

days = 30
start_price = 100

daily_returns = np.random.normal(0.001, 0.02, days)

price_series = start_price * np.cumprod(1 + daily_returns)

df = pd.DataFrame({
    "Day": range(1, days + 1),
    "Stock_Price": price_series
})

print(df)
print("\nFinal Price:", df["Stock_Price"].iloc[-1])