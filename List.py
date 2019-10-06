fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
2
fruits.append('coconut')
fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
fruits.extend('cucumber')
fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut', 'c', 'u', 'c', 'u', 'm', 'b', 'e', 'r']

fruits.extend('apple')
fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut', 'c', 'u', 'c', 'u', 'm', 'b', 'e', 'r', 'a', 'p', 'p', 'l', 'e']

fruits.extend('smz')
fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut', 'c', 'u', 'c', 'u', 'm', 'b', 'e', 'r', 'a', 'p', 'p', 'l', 'e', 's', 'm', 'z']

fruits.clear()
fruits
[]

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'coconut']
fruits.reverse()
fruits
['coconut', 'banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.count('banana')
2
fruits.count('kiwi')
1
fruits.index('kiwi')
3
>>> fruits.index('pear')
5
>>> fruits.index('apple')
2
>>> fruits.index('apple')
2
>>> fruits.index('apple')
2
>>> fruits.index('apple')
2

 fruits.sort()
fruits
['apple', 'apple', 'banana', 'banana', 'coconut', 'kiwi', 'orange', 'pear']

fruits.pop()
'pear'
fruits
['apple', 'apple', 'banana', 'banana', 'coconut', 'kiwi', 'orange']

fruits.remove('kiwi')
fruits
['apple', 'apple', 'banana', 'banana', 'coconut', 'orange']

student = ['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko']
student
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko']

student.append('Phyu Phyu')
student.append('Ni Ni')
student
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']

student.remove('Mya Mya')
student
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']

student.pop()
'Ni Ni'

student
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu']

from collections import deque
queue = deque(["Eric", "John", "Micheal"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
'Eric'
queue
deque(['John', 'Micheal', 'Terry', 'Graham'])

cube = []
for i in range(30):
     cube.append(i**3)

cube
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000, 9261, 10648, 12167, 13824, 15625, 17576, 19683, 21952, 24389]

cube = list(map(lambda x: x**3, range(10)))
cube
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cube = [x**3 for x in range(10)]
cube
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# cube သုံးခုလုံးကတူတူပဲ။ ရေးသားပုံပဲကွာတယ်။

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

combs = []
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if x != y:
			combs.append((x, y))

combs
#အပေါ်ကနှစ်ခုကအဖြေတူတူပဲ

 matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
