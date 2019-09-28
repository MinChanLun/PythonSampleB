# f = open('test.txt', 'r') # r stands for read.

# print(f.name)

# f.close()

# with open('test.txt', 'a') as g:#a = append
# 	g.write('6. This is Line Number 6.' + "/n")
# 	print(g, end='')		

with open('test.txt', 'r') as f:

	#f_text = f.readline()
	#print(f_text, end='') end='' ကိုစာကြောင်းတွေကပ်နေတာကိုဖြေရှင်းဖို့။


	# for i in f:
	# 	print(i, end='')

	# f_text = f.read(500)
	# print(f_text, end='')

	# with open('test.txt', 'a') as g:
	# i = g.write('6. This is Line number 6.' + "\n")
	# print(g.write(i, end=''))

	# g = open('test.txt', 'a')
	# i = g.write('6. This is Line Number 6.')
	# print(i, end ='')

	size_to_read = 500
	f_text = f.read(size_to_read)

	while len(f_text) > 0:
		print(f_text, end='')
	

