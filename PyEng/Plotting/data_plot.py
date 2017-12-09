#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

salary = np.fromfile('salaries.txt', dtype=int, sep=',')
names = np.genfromtxt('names.txt', dtype='str', delimiter=',')

print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

x = np.arange(len(names))
plt.bar(x, salary)
plt.xticks(x, names)
plt.ylabel('Salaries')
plt.xlabel('Names')
plt.title('Salary of 10 random people')
plt.show()

# remove extreme values which may be interfering with results
salaries_new = salary[2:-2]
names_new = names[2:-2]

print(np.max(salaries_new), np.min(salaries_new), np.average(salaries_new))

x = np.arange(len(names_new))
plt.bar(x, salaries_new)
plt.xticks(x, names_new)
plt.show()

