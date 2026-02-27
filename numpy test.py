import numpy as np
import pandas as pd

arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Mean:", np.mean(arr))

data = {
    "Name": ["Yoges", "Arun", "Kumar"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print("\nStudent Data:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())