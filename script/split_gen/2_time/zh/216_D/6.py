def solve(N, M, k, a):
    if M % 2 == 1:
        return False
    for i in range(M // 2):
        if len(a[2 * i] & a[2 * i + 1]) == 0:
            return False
    return True
N, M = map(int, input().split())
k = [0] * M
a = [set() for _ in range(M)]
for i in range(M):
    k[i] = int(input())
    a[i] = set(map(int, input().split()))
print("Yes" if solve(N, M, k, a) else "No")
