#x = int(input("Please enter an integer: "))

#if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

#Single 

x = int(input("Please Enter your Marks: "))
if x == 100:
     print('You have accessed to the Heaven!!')
elif x >= 70 and x < 100:
     print('You have passed the exam with wings.')
elif x >= 50 and x < 70:
     print('You are excellent.')
elif x >= 40 and x < 50:
 	print('Pass!')
elif x >= 35 and x < 40:
	if x == 39:
		print ('39 + 1 and you pass.')
	elif x == 38:
		print ('38 + 2 and you pass.')
	elif x == 37:
		print ('37 + 3 and you pass.')
	elif x == 36:
		print ('36 + 4 and you pass.')
	elif x == 35:
		print ('35 + 5 and you pass.')
elif x > 10 and x < 35:
	print('Fail!')
elif x <= 10 and x >0:
	print('Call your parenets.')
else:
	print('You are not qualified.')