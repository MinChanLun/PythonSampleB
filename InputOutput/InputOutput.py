#Week 6A 19. 10. 2019

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
#'Results of the 2016 Referendum'

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{: -9} YES votes {: 2.2%}'.format(yes_votes, percentage)

str(s)
repr(s)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '.'
print(s)

hello = 'hello, world \n'
hellos = repr(hello)
print(hellos)

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.

 table = {'Sjoerd': 4127, 'Jack' : 4098, 'Dcab' : 7678}
 for name, phone in table.items():
     print(f'{name:10} ==> {phone:10d}'
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.

print ('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

print('This {food} is {adjective}.'.format(
     food = 'spam', adjective = 'absolutely horrible'))
This spam is absolutely horrible.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Mangred', other = 'Georg'))
The story of Bill, Mangred, and Georg.

table = {'Sjoerd' : 4127, 'Jack' : 4098, 'Dcab' : 8637678}
print('Jack : {0[Jack]:d}; Sjoerd : {0[Sjoerd]:d}; ' 'Dcab : {0[Dcab]:d}'.format(table))
Jack : 4098; Sjoerd : 4127; Dcab : 8637678
print('Jack : {Jack:d}; Sjoerd : {Sjoerd:d}; Dcab : {Dcab:d}'.format(**table))
Jack : 4098; Sjoerd : 4127; Dcab : 8637678

 for x in range(1, 11):
     print(' {0:2d} {1:3d} {2:4d} '.format(x, x*x, x*x*x))

  1   1    1
  2   4    8
  3   9   27
  4  16   64
  5  25  125
  6  36  216
  7  49  343
  8  64  512
  9  81  729
 10 100 1000

for x in range(1, 11):
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     print(repr(x*x*x).rjust(4))

 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000

'12'.zfill(5)
'00012'
'-3.14'.zfill(7)
'-003.14'
'3.14159265359'.zfill(5)
'3.14159265359'

 print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.