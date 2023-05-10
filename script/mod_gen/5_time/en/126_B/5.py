def main():
	s = input()
	if int(s[:2]) in range(1,13) and int(s[2:]) in range(1,13):
		print('AMBIGUOUS')
	elif int(s[:2]) in range(1,13):
		print('MMYY')
	elif int(s[2:]) in range(1,13):
		print('YYMM')
	else:
		print('NA')

if __name__ == '__main__':
    main()