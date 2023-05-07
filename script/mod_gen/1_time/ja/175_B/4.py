def check(a,b,c):
    if a == b or b == c or c == a:
        return False
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if check(L[i],L[j],L[k]):
                ans += 1
print(ans)

if __name__ == '__main__':
    check()