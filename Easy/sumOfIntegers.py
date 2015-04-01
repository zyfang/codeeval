import sys
test_cases = open('inputest.txt', 'r')
sumn = 0
for test in test_cases:
    numbers = test.split(',')
    a = int(numbers[0])
    b = int(numbers[1])
    c = a/b
    d = a-(c*b)
    print d
test_cases.close()
