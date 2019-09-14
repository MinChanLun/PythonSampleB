#Week 2A 14.9.2019

print('"I can do everything Nothing Impossible"')
print("'I can do everything Nothing Impossible'")

x = 'Hello World'
print(x)

print('doesn\'t')
#doesn't

print('\"Yes,\" they said.')
"Yes," they said.

>>> 5 * 'Hello' + 'World'
'HelloHelloHelloHelloHelloWorld'
>>> x = 'Hello' + 'World'
>>> x
'HelloWorld'
>>> x = 'Hello' + ' ' + 'World'
>>> x
'Hello World'
>>> 'Helllo' + str(3)
'Helllo3'
>>> int('3') + 3
6
>>> int("3") + 3
6

#String
P r o g r a m m i n g
0 1 2 3 4 5 6 7 8 9 10
-11 -9 -8 -7 -6 -5 -4 -3 -2 -1
x = 'Programming'
x[6] #Choosing the column
'm'

>>> x = 'Programming'
>>> x[6]
'm'
>>> x[0]
'P'
>>> x[0:6]
'Progra'
>>> x[1:5]
'rogr'
>>> x[2:5]
'ogr'
>>> x[:7]
'Program'
>>> x[8:]
'ing'
>>> x[:]
'Programming'
>>> x[]
  File "<stdin>", line 1
    x[]
      ^
SyntaxError: invalid syntax
>>> x[-4]
'm'
>>> x[5:-4]
'am'

>>> x = 'Programming'
>>> x[:3] + x[4:]
'Proramming'

>>> x = 'Programming'
>>> x[0] = 'Q' #replace Q in P
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
#len = length
>>> len(x) + 4
15
>>> len(x[5]) + 4
5
>>> len(x[5])
1
>>> len(x[5:9]) + 4
8

#List
>>> word = [ 1, 3, 5, 7, 9, 11, 13, 15]
>>> word
[1, 3, 5, 7, 9, 11, 13, 15]
>>> word[5]
11
word[4] = 10 #change value

>>> word = ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
>>> word
['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
>>> word[0] = 'Q'
>>> word
['Q', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
>>> word[:] = 'Good'
>>> word
['G', 'o', 'o', 'd']
>>> word[3]
'd'

>>> word = [1, 3, 5, 7, 9, 11, 13, 15]
>>> word
[1, 3, 5, 7, 9, 11, 13, 15]
>>> word + word
[1, 3, 5, 7, 9, 11, 13, 15, 1, 3, 5, 7, 9, 11, 13, 15]
>>> word[:] + [ 2, 4, 6, 8, 10]
[1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10]

>>> a = [ 1, 3, 5, 7, 9]
>>> b = [ 2, 4, 6, 8, 10]
>>> x = a + b
>>> x
[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

>>> c = [ 'A', 'B', 'C', 'D', 'E']
>>> x = a + b + c
>>> x
[1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 'A', 'B', 'C', 'D', 'E']
>>> x = [a, b, c]
>>> x
[[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], ['A', 'B', 'C', 'D', 'E']]
>>> x[1:3]
[[2, 4, 6, 8, 10], ['A', 'B', 'C', 'D', 'E']]