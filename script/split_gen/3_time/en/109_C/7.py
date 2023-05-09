def find_gcd(a,b):
    if b == 0:
        return a
    else:
        return find_gcd(b,a%b)
n,x = map(int,input().split())
x_list = list(map(int,input().split()))
x_list.append(x)
x_list.sort()
diff_list = []
for i in range(n):
    diff_list.append(x_list[i+1]-x_list[i])
gcd = diff_list[0]
for i in range(n-1):
    gcd = find_gcd(gcd,diff_list[i+1])
print(gcd)
