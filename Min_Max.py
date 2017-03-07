def find_max_min(myList):
  
	myList.sort()
	
	if myList[0] != myList[-1]:
	  
	  return [myList[-len(myList)], myList[-1]]
	  
	else:
	  
	  return [len(myList)]