import pandas as pd

try:
    # Adjust the path if the file is in a different location
    data = pd.read_json("names1.json")
    print(data)
except ValueError as e:
    print("Error reading JSON:", e)
