def main():
	nums = input().split()
	A = int(nums[0])
	B = int(nums[1])
	T = int(nums[2])
	sum = 0
	for i in range(1, T+1):
		if (i % A == 0):
			sum += B
	print(sum)

if __name__ == '__main__':
    main()