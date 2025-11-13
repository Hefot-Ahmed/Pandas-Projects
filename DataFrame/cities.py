import pandas as pd
data = {
    'City': ['Brooklyn', 'Seoul', 'Barcelona'],
    'Country': ['US', 'South Korea', 'Spain'],
    'Population': [2617631, 9000000, 1730398], 
}

df = pd.DataFrame(data)
print(df)
