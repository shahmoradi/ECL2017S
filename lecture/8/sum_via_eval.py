import sys
print( 'The sum of {} is {}'.format( ' '.join(sys.argv[1:]) , eval('+'.join(sys.argv[1:]) ) ) )