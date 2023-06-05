def gcd(a,b):
	while b:
		a,b = b,a%b
	return a
n,m = map(int,input().split())

if __name__ == '__main__':
    gcd()