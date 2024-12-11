import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Create the dataset using Pandas
data = {
    'Bedrooms': [1, 1, 2, 2, 3, 3],
    'Price': [80000, 90000, 100000, 90000, 100000, 90000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Prepare the data (independent variable and dependent variable)
X = df[['Bedrooms']]  # Independent variable (Number of Bedrooms)
y = df['Price']       # Dependent variable (Price)

plt.scatter(X, y, color='blue', label='Data points')

# Adding titles and labels
plt.title('Number of Bedrooms vs. Price (Without Line of Best Fit)')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')

# Display the legend
plt.legend()

# Step 4: Save the plot locally as an image
plt.savefig('./scatter_plot_without_line_of_best_fit.png')