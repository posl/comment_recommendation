def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a = list(set(a))
# print(a)
ans = []
for i in range(1,m+1):
    flag = True
    for j in range(len(a)):
        if gcd(a[j],i) != 1:
            flag = False
            break
    if flag:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

if __name__ == '__main__':
    gcd()