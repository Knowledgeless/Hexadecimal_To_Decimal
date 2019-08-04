###############################################	
#					      #
#	 Convert From Hexadecimal To Decimal  #
#					      #
###############################################

print('''
	----------------
	 Hex to Decimal
	----------------
''')

def con(n,b):
	x = n.upper()	 # If user input small char it will convert into upper char
	d = len(n)-1
	l = 0
	for i in x:
		if(i > "F"):	 # User may input more than 'f/F' which is incorrect.
			print("Invalid Input According To Base")
			exit()
		else:
			h = int(i, 16)
			l += h*(b**d)		# Formula to convert the base
			d = d-1
	print(l)					# Printing the result

n = input("Enter The Hexadecimal Value: ")
b = 16
print("Your Decimal Value Is: ")
con(n,b) 
