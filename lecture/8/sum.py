import sys
print( 'The sum of {} is {}'.format( ' '.join(sys.argv[1:]) , sum([float(x) for x in sys.argv[1:]]) ) )