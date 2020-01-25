def returnEncodingString(inputString): 
	returnString = ''
	repeats = 0
	if inputString == '':
		return ''
	else:
        print('hey running!')
		for i in range(0, len(inputString) - 1):
			if inputString[i] != inputString[i+1]: #stops repeating
				returnString += inputString[i] * repeats 
				repeats = 1
			else: #repeating 
				repeats += 1 
	return returnString 
	
print(returnEncodingString('wwwwaaadexxxxxx'))
				