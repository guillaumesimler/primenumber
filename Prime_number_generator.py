''' A program by Guillaume Simler

More a test for algorythms than anything else'''

def prime_check(figu, input_list):
# not planed for list below 3
	for n in range (1, len(input_list)):
		if figu % input_list[n] == 0:
			return False

	return True	

def prime_generator(figu):
	output_r = []

	if figu <= 3:
		for n in (1,figu+1):
			output_r.append(n)
		return output_r

	output_r = [1,2,3]

	for n in range (4,figu + 1):
		
		if prime_check(n, output_r):
			output_r.append(n)

	return output_r

print prime_generator(200000)


