PAGE_CNT = 5

def transInt (value):
	try:
		if isinstance(value, int) is False : value = int(value);
	except ValueError, e:
		value=0

	return value

def transStr (value):
	if isinstance(value, str) is False :
		value = str(value).decode('utf-8')
	return  value


def getInterval (start, end):
	""" get Broad Interval """
	start = transInt(start)
	end = transInt(end)

	startNum = end * PAGE_CNT
	endNum = startNum + PAGE_CNT
	if endNum > start:
		endNum = start

	return startNum, endNum