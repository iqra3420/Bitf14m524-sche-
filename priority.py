processes = int(input('Enter no. of process :  '))
dict = {}

process_id = []
for index in range(processes):
    arrival_t_input = int(input('Enter arrival time :  '))
    burst_t_input = int(input('Enter burst time :  '))
    priority_input = int(input('Enter priority :  '))
    process_id.append(index)
    dict[int(index)] = [arrival_t_input, burst_t_input,priority_input]

print"Processes   Arrival Time   Burst Time   Priority "
for index in range(len(dict)):
    print index + 1, "       |     ", dict[int(index)][0], "      |      ", dict[int(index)][1], "      |      ", dict[int(index)][2]

start_t = {}
dict2 = dict.copy()
time = 0
calWait = 0.0
cal_burst = 0
dict_index = 0
dict_arrival = 0
dict_burst = 0
dict_priority =0
p_index = 0
while 1:
    if len(dict) == 0:
        break
    for index in range(len(process_id)):
            dict_index = process_id[index]
            dict_arrival = dict[process_id[index]][0]
            dict_burst = dict[process_id[index]][1]
            dict_priority = dict[process_id[index]][2]
            p_index = index
            break
    for index in range(len(process_id)):
            if dict[dict_index][0] >= dict[process_id[index]][0] and dict[dict_index][2] > dict[process_id[index]][2]:
                dict_index = process_id[index]
                p_index = int(index)
                dict_arrival = dict[process_id[index]][0]
                dict_burst = dict[process_id[index]][1]
                dict_priority = dict[process_id[index]][2]

    del dict[dict_index]
    del process_id[p_index]

    check_arrival = 0
    cal_burst = 0

    while dict_burst != cal_burst:
        if dict_arrival <= time:
            cal_burst += 1
            if check_arrival == 0:
                start_t[int(dict_index)] = time
                check_arrival = 1
        time += 1

print "\nStart Time    arrival Time   waiting Time "
for index in range(len(dict2)):
    ProcessWait = start_t[index] - dict2[int(index)][0]
    calWait += ProcessWait
    print start_t[int(index)], "             ", (dict2[int(index)][0]), "            ", ProcessWait
print "\nThe average waiting time :", calWait / processes
raw_input()
