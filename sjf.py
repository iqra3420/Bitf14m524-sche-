processes = int(input('Enter no. of process :  '))
dictonary = {}

process_id = []
for x in range(processes):
    arrival_time = int(input('Enter arrival time :  '))
    burst_time = int(input('Enter burst time :  '))
    process_id.append(x)
    dictonary[int(x)] = [arrival_time, burst_time]

print"Processes   Arrival Time   Burst Time "
for x in range(len(dictonary)):
    print x + 1, "       |     ", dictonary[int(x)][0], "      |      ", dictonary[int(x)][1]

start_time = {}
dictonary2 = dictonary.copy()
time = 0
Wait = 0
burst = 0
dictonary_index = 0
dictonary_arrival = 0
dictonary_burst = 0
p_index = 0
while 1:
    if len(dictonary) == 0:
        break
    for x in range(len(process_id)):
            dictonary_index = process_id[x]
            dictonary_arrival = dictonary[process_id[x]][0]
            dictonary_burst = dictonary[process_id[x]][1]
            p_index = x
            break
    for x in range(len(process_id)):
            if dictonary[dictonary_index][0] >= dictonary[process_id[x]][0] and dictonary[dictonary_index][1] > dictonary[process_id[x]][1]:
                dictonary_index = process_id[x]
                p_index = int(x)
                dictonary_arrival = dictonary[process_id[x]][0]
                dictonary_burst = dictonary[process_id[x]][1]

    del dictonary[dictonary_index]
    del process_id[p_index]

    check_arrival = 0
    burst = 0

    while dictonary_burst != burst:

        if dictonary_arrival <= time:
            burst += 1
            if check_arrival == 0:
                start_time[int(dictonary_index)] = time
                check_arrival = 1
        time += 1

print "Start Time    arrival Time   waiting Time "
for x in range(len(dictonary2)):
    ProcessWait = start_time[x] - dictonary2[int(x)][0]
    Wait += ProcessWait
    print start_time[int(x)], "             ", (dictonary2[int(x)][0]), "            ", ProcessWait
print "The average waiting time :", Wait / processes
raw_input()
