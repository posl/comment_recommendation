def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(set(a))
cnt = 0
ans = []
for i in range(1, m+1):
    flag = True
    for j in range(len(a)):
        if gcd(a[j], i) != 1:
            flag = False
            break
    if flag:
        cnt += 1
        ans.append(i)
print(cnt)
for i in range(len(ans)):
    print(ans[i])

if __name__ == '__main__':
    gcd()