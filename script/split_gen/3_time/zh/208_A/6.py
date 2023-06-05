def is_sum_possible(a, b):
	if a > b:
		return False
	if a * 6 < b:
		return False
	return True
