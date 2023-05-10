def gcd(a,b):
	while b:
		a,b = b,a%b
	return a
n,m = map(int,input().split())
a = list(map(int,input().split()))
l = [0]*(m+1)
for i in a:
	for j in range(1,int(m/i)+1):
		l[i*j] = 1
ans = []
for i in range(1,m+1):
	if not l[i]:
		ans.append(i)
print(len(ans))
for i in ans:
	print(i)

if __name__ == '__main__':
    gcd()