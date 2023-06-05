def main():
	# get input
	sheep, wolf = map(int, input().split())
	# judge
	if wolf >= sheep:
		print("不安全")
	else:
		print("安全")

if __name__ == '__main__':
    main()