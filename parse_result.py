import sys
import csv

if len(sys.argv) < 2:
    print('Error: requires a file to parse.')
    sys.exit(1)

# Set the number of repeated experiments
num_exp = 5

# Open the result file to parse
result_file = open('results/' + sys.argv[1], 'r')
lines = result_file.readlines()

# Parse the result file into list
res = []
cc = ''
thread = 0
warehouse = 0
throughput = 0
abort_rate = 0
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
        idx = line.find('s=') + 2
        commaidx = line.find(',')
        thread = int(line[idx:commaidx])
        idx = line.find('m=') + 2
        warehouse = int(line[idx:])
    elif 'RESULT' in line:
        # Result line
        idx = line.find('t(') + 2
        commaidx = line.find(',')
        throughput = float(line[idx:commaidx-1])
        idx = line.find('e(') + 2
        abort_rate = float(line[idx:len(line)-2])
        # Store in res
        res.append([cc, thread, warehouse, throughput, abort_rate])
    else:
        continue

# Calculate the average throughput, abort rate, and plot the result
exp_res = []
cnt = 0
avg_throughput = 0
avg_abort_rate = 0
for row in res:
    cnt += 1
    avg_throughput += row[3]
    avg_abort_rate += row[4]
    if cnt == num_exp:
        avg_throughput /= num_exp
        avg_abort_rate /= num_exp
        exp_res.append([row[0], row[1], row[2], avg_throughput, avg_abort_rate])
        cnt = 0
        avg_throughput = 0
        avg_abort_rate = 0

# Create a csv file and store parsed results
csv_file = open('csvs/' + sys.argv[1] + '.csv', 'w')
writer = csv.writer(csv_file)
for row in exp_res:
    writer.writerow(row)

# Close files
result_file.close()
csv_file.close()
print('Parse complete. Result stored in csvs/' + sys.argv[1] + '.csv')
