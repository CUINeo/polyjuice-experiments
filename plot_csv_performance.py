import sys
import csv
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('Error: requires a csv file to plot.')
    sys.exit(1)

thread = 48
res = {'Polyjuice': [[], [], []], 'Silo': [[], [], []], '2PL': [[], [], []]}

with open('csvs/' + sys.argv[1] + '.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        res[row[0]][0].append(row[2]) 
        res[row[0]][1].append(row[3])
        res[row[0]][2].append(row[4])
csv_file.close()

fig, axs = plt.subplots(3, 2)

cc = 'Polyjuice'
axs[0, 0].plot(res[cc][0], res[cc][1], label='Throughput')
axs[0, 0].set_title(cc + ' (' + str(thread) + ' threads)')
axs[0, 1].plot(res[cc][0], res[cc][2], label='Abort rate')
axs[0, 1].set_title(cc + ' (' + str(thread) + ' threads)')

cc = 'Silo'
axs[1, 0].plot(res[cc][0], res[cc][1], label='Throughput')
axs[1, 0].set_title(cc + ' (' + str(thread) + ' threads)')
axs[1, 1].plot(res[cc][0], res[cc][2], label='Abort rate')
axs[1, 1].set_title(cc + ' (' + str(thread) + ' threads)')

cc = '2PL'
axs[2, 0].plot(res[cc][0], res[cc][1], label='Throughput')
axs[2, 0].set_title(cc + ' (' + str(thread) + ' threads)')
axs[2, 1].plot(res[cc][0], res[cc][2], label='Abort rate')
axs[2, 1].set_title(cc + ' (' + str(thread) + ' threads)')

plt.savefig('figures/' + sys.argv[1] + '.png')
print('Plot complete. Result figure stored in figures/' + sys.argv[1] + '.png')
