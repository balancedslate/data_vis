import matplotlib.pyplot as plt

# Data to plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create a bar chart
plt.bar(x, y, color="orange", alpha=0.5)

# Add axis labels and a title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("My Bar Chart")

# Show the plot
plt.show()
