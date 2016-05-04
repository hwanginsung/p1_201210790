sumOfMen=0
sumOfWomen=0
avgOfMen=0
avgOfWomen=0
sumOfLocal=dict()
for i in range(0,len(population)):
    sumOfMen+=population[i][0]
    sumOfWomen+=population[i][1]
    avgOfMen=sumOfMen/25
    avgOfWomen=sumOfWomen/25
    sumOfLocal[i]=population[i][0]+population[i][1]

print sumOfMen
print sumOfWomen
print avgOfMen
print avgOfWomen
print sumOfLocal

%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

plt.bar(range(len(population)),sumOfLocal.values())