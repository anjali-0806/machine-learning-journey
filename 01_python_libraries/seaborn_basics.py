
# Machine Learning Journey
# Topic: Introduction to Seaborn

import seaborn as sns
import matplotlib.pyplot as plt

# Loading an inbuilt dataset
data = sns.load_dataset("iris")

# Displaying first five rows
print(data.head())

# Scatter plot
sns.scatterplot(data=data, x="sepal_length",
                y="petal_length")

plt.title("Sepal Length vs Petal Length")
plt.show()

# Histogram
sns.histplot(data=data, x="sepal_length")

plt.title("Sepal Length Distribution")
plt.show()

# Box plot
sns.boxplot(data=data, x="species",
            y="sepal_length")

plt.title("Sepal Length by Species")
plt.show()

# Heatmap of numerical correlations
correlation = data.select_dtypes(
    include="number"
).corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()
