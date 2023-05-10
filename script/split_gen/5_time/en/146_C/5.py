def d(n):
    return len(str(n))
a,b,x = map(int, input().split())
ans = 0
for i in range(1,11):
    if a*i + b*d(i) <= x:
        ans = i
    else:
        break
print(ans)
