import sys
test_cases = open('inputest.txt', 'r')
for test in test_cases:
    maxsum = 0
    temp = test.split(';')
    ndays = int(temp[0]) #how many days to invest
    listgains = temp[1].rstrip().split(' ') #put gains and losses each day in a list
    for iday in xrange(len(listgains)-ndays+1): #for each possible starting day, check value after investing ndays
        isum = 0
        for i_nday in xrange(iday,iday+ndays): #get sum of next n days
            isum += int(listgains[i_nday])
        if isum > maxsum: #If the max sum for this iday is greater than any maxsum we had before
            maxsum = isum
    print maxsum
test_cases.close()