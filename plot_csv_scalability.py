import sys
import csv
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('Error: requires a csv file to plot.')
    sys.exit(1)

warehouse = 1
res = {'Polyjuice': [[], [], []], 'Silo': [[], [], []], '2PL': [[], [], []]}

with open('csvs/' + sys.argv[1] + '.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        res[row[0]][0].append(int(row[1])) 
        res[row[0]][1].append(float(row[3]))
        res[row[0]][2].append(float(row[4]))
csv_file.close()

fig, axs = plt.subplots(2)
fig.tight_layout()

# Throughput subplot
axs[0].set_title('Throughput' + ' (' + str(warehouse) + ' warehouses)')
axs[0].plot(res['Polyjuice'][0], res['Polyjuice'][1], 'tab:blue', label='Polyjuice')
axs[0].plot(res['Silo'][0], res['Silo'][1], 'tab:green', label='Silo')
axs[0].plot(res['2PL'][0], res['2PL'][1], 'tab:red', label='2PL')
axs[0].legend()

# Abort rate subplot
axs[1].set_title('Abort rate' + ' (' + str(warehouse) + ' warehouses)')
axs[1].plot(res['Polyjuice'][0], res['Polyjuice'][2], 'tab:blue', label='Polyjuice')
axs[1].plot(res['Silo'][0], res['Silo'][2], 'tab:green', label='Silo')
axs[1].plot(res['2PL'][0], res['2PL'][2], 'tab:red', label='2PL')
axs[1].legend()

for ax in axs.flat:
    ax.set(xlabel='Thread')

plt.savefig('figures/' + sys.argv[1] + '.png')
print('Plot complete. Result figure stored in figures/' + sys.argv[1] + '.png')
plt.show()
