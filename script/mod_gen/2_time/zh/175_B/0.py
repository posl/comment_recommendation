def check(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if check(L[i], L[j], L[k]) and L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                ans += 1
print(ans)

if __name__ == '__main__':
    check()