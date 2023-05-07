def d(n):
    if n == 0:
        return 1
    else:
        return len(str(n))
a, b, x = map(int, input().split())
ans = 0
for i in range(1, 10**9+1):
    if a*i + b*d(i) > x:
        break
    else:
        ans = i
print(ans)
