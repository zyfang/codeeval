import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    testlist = test.rstrip().split(',')
    digitlist = []
    wordlist = []
    for el in testlist:
        if el.isdigit():
            digitlist.append(el)
        else:
            wordlist.append(el)
    if wordlist and digitlist:
        print ','.join(wordlist) + '|' + ','.join(digitlist)
    elif wordlist:
        print ','.join(wordlist)
    elif digitlist:
        print ','.join(digitlist)
test_cases.close()