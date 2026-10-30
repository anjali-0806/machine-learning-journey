
# ==========================================
# MACHINE LEARNING JOURNEY
# Topic: Introduction to Matplotlib
# ==========================================

# Importing Matplotlib
import matplotlib.pyplot as plt

# Creating dataset
hours = [1, 2, 3, 4, 5, 6]
marks = [20, 35, 45, 60, 70, 85]

# Creating a line graph
plt.plot(hours, marks)

# Adding graph title
plt.title("Study Hours vs Marks")

# Naming X-axis
plt.xlabel("Hours Studied")

# Naming Y-axis
plt.ylabel("Marks Obtained")

# Displaying grid
plt.grid()

# Displaying graph
plt.show()


# Creating a scatter plot
plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")

plt.grid()
plt.show()


# Creating a bar graph
plt.bar(hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")

plt.show()
