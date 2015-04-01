import sys
test_cases = open('inputest.txt', 'r')
sumn = 0
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    numb = int(test)
    sumn = sumn + numb
print sumn
test_cases.close()
