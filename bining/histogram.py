import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(1)

# Create DataFrame
df = pd.DataFrame({
    'team': np.repeat(['A', 'B', 'C'], 100),  # Repeat 'A', 'B', 'C' each 100 times
    'points': np.random.normal(loc=20, scale=2, size=300)  # Generate 300 normally distributed points
})

# View the first few rows of the DataFrame to confirm its structure
# print(df.head())

# print(df)
# Create a histogram with 20 bins and black edges for each bin
df.plot.hist(column='points', edgecolor='black', bins=20)

# Display the histogram
plt.show()
