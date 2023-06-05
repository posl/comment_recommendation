def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 1
    for i in range(1, N+1):
        ans = max(ans, A.count(i), B.count(i))
    print(ans)
