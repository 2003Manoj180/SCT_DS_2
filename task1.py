import matplotlib.pyplot as plt

# Age groups
age_groups = ["0-20", "21-64", "65+"]
population = [512, 807, 98]   # in millions
percent = [36.1, 57.0, 6.9]

# Create bar chart
plt.bar(age_groups, population, color=["gold", "deepskyblue", "hotpink"])

# Add labels
for i, (pop, pct) in enumerate(zip(population, percent)):
    plt.text(i, pop + 10, f"{pop}M\n{pct}%", ha='center', fontsize=10)

plt.title("India's Population Distribution by Age (2022)")
plt.ylabel("Population (Millions)")
plt.show()