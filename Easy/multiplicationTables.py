import sys

#for each number up to 12, print a line
for irow in xrange(1,13):
    for icol in xrange(1,13):
        val = irow*icol
        sys.stdout.write('%4d' % val)
    sys.stdout.write('\n')