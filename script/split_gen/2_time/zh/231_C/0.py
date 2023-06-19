def main():
	n, q = map(int, input().split())
	student = list(map(int, input().split()))
	student.sort()
	for i in range(q):
		x = int(input())
		# 二分查找
		low = 0
		high = n
		while low < high:
			mid = (low + high) // 2
			if student[mid] >= x:
				high = mid
			else:
				low = mid + 1
		print(n - low)
