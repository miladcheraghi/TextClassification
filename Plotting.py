import matplotlib.pyplot as plt
import pandas as pd


result = pd.read_csv("Bag_of_Words_model.csv", header=0, \
                    delimiter=",", quoting=2)

sumPolitical = 0
print(result['id'][1] , result['class'][1] )
for row in result['class']:
    print(row)
    if row == 1 :
        sumPolitical = sumPolitical + 1
sumNonPolitical = len(result) - sumPolitical


# Data to plot
labels = 'Political', 'Unpolitical'
sizes = [sumPolitical, sumNonPolitical]
colors = [ 'lightcoral', 'lightskyblue']    # , 'lightcoral', 'lightskyblue'
explode = (0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
