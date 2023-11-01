def main():
	n = int(input())
	if n % 10 == 7:
		print("Yes")
	elif n // 10 % 10 == 7:
		print("Yes")
	elif n // 100 % 10 == 7:
		print("Yes")

if __name__ == '__main__':
    main()