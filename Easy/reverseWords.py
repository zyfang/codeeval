import sys

test_cases = open('inputest.txt', 'r')
for test in test_cases:
    allwords = test.rstrip().split(' ')
    for i in xrange(len(allwords)-1, 0, -1):
        sys.stdout.write(allwords[i] + ' ')
    sys.stdout.write(allwords[0]+'\n')
test_cases.close()
