def main():
	n = int(input())
	trees = [int(i) for i in input().split()]
	
	count = 0
	for tree in trees:
		if tree > 10:
			count += tree - 10
	print(count)
