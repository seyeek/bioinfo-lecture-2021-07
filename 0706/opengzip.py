import sys
import gzip
g_bfile = gzip.open(sys.argv[1],'rb')
if sys.argv[1][-2:] == 'gz':
    gb_file = gzip.open(sys.argv[1],'rb')
else:
    gb_file = open(sys.argv[1],'r')
