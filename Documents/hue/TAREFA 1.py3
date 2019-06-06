x=1
while x <= 100:
	if (x % 15) == 0:
		print("QuantoSobra")
	elif (x % 3) == 0:
		print("Sobra")
	elif (x % 5) == 0:
		print("Quanto")
	else:
		print(x)
	x=x+1