def words(text):
	
	word_list = text.split()
	text_dict = {}
	
	for item in word_list:
		if item in text_dict:
			continue
		else:
			text_dict[item] = word_list.count(item)

	nums = {}

	for item in text_dict.items():
		if item[0].isdigit():
			nums[int(item[0])] = item[1]
		else:
			nums[item[0]] = item[1]

	return nums