import numpy as np

scores = np.array([45, 67, 89, 34, 90, 55, 76])

mask = scores >= 60

failed = scores[scores<40]

scores[scores<50] += 10

print(scores[mask])
print(failed.size)
print(scores)
print("\n")
marks = np.array([
    [78, 85, 90],
    [62, 70, 60],
    [92, 88, 95],
    [45, 50, 55]
])

min_values = np.min(marks , axis=0)
max_values = np.max(marks , axis=0)

normalized = (marks-min_values) / (max_values - min_values)

marks[marks<50] += 5

print(normalized)
print(marks)
