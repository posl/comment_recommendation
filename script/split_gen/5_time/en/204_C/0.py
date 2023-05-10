def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            if A.count(i) > 0 and B.count(j) > 0:
                ans += 1
    print(ans)
