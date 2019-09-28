#B 22. 9. 2019
for i in range(5):
	print(i)

for i in range(5):
	for i in range(i):
		print(i)

for i in range(3):
	for j in range(i):
		for x in range(j):
			print(x)

a = ['Marry', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
...     print(i, a[i])
...
0 Marry
1 had
2 a
3 little
4 lamb

