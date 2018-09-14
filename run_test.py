import numpy as np

age = np.loadtxt('participants.tsv', skiprows=1, usecols=1)
mean_age = sum(age)/len(age)
np.savetext('demeandd_age.txt', age-mean_age)
print('done')
