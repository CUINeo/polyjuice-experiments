import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('Error: requires a result file to plot.')
    sys.exit(1)

num_exp = 5
num_latency = 9
thread = 48
warehouse = 1

result_file = open('results/' + sys.argv[1], 'r')
lines = result_file.readlines()

res = {'Polyjuice': [], 'Silo': [], '2PL': []}
for key, val in res.items():
    for i in range(num_latency):
        val.append(0)

for line in lines:
    if 'tpc-c.' in line:
        # Info line
        idx = line.find('c=') + 2
        if line[idx] == 'P':
            cc = 'Polyjuice'
        elif line[idx] == 'S':
            cc = 'Silo'
        else:
            cc = '2PL'
        # idx = line.find('s=') + 2
        # commaidx = line.find(',')
        # thread = int(line[idx:commaidx])
        # idx = line.find('m=') + 2
        # warehouse = int(line[idx:])
    elif 'new_order_p50' in line:
        idx = line.find('y -') + 4
        res[cc][0] += (float(line[idx:]))
    elif 'new_order_p90' in line:
        idx = line.find('y -') + 4
        res[cc][1] += (float(line[idx:]))
    elif 'new_order_p99' in line:
        idx = line.find('y -') + 4
        res[cc][2] += (float(line[idx:]))
    elif 'payment_p50' in line:
        idx = line.find('y -') + 4
        res[cc][3] += (float(line[idx:]))
    elif 'payment_p90' in line:
        idx = line.find('y -') + 4
        res[cc][4] += (float(line[idx:]))
    elif 'payment_p99' in line:
        idx = line.find('y -') + 4
        res[cc][5] += (float(line[idx:]))
    elif 'delivery_p50' in line:
        idx = line.find('y -') + 4
        res[cc][6] += (float(line[idx:]))
    elif 'delivery_p90' in line:
        idx = line.find('y -') + 4
        res[cc][7] += (float(line[idx:]))
    elif 'delivery_p99' in line:
        idx = line.find('y -') + 4
        res[cc][8] += (float(line[idx:]))
    else:
        continue

for key, val in res.items():
    for i in range(len(val)):
        val[i] /= num_exp

labels = ['new_order_p50', 'new_order_p90', 'new_order_p99', 'payment_p50',
    'payment_p90', 'payment_p99', 'delivery_p50', 'delivery_p90', 'delivery_p99']

x = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, res['Polyjuice'], width, label='Polyjuice')
rects2 = ax.bar(x, res['Silo'], width, label='Silo')
rects3 = ax.bar(x + width, res['2PL'], width, label='2PL')

ax.set_ylabel('Latency - µs')
ax.set_title('Latency of three CC algorithms')
ax.set_xticks(x, labels)
ax.legend()

# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)
# ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.savefig('figures/' + sys.argv[1] + '.png')
print('Plot complete. Result figure stored in figures/' + sys.argv[1] + '.png')
plt.show()

result_file.close()
