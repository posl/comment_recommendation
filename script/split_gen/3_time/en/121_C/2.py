def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = list(zip(A, B))
    C.sort()
    ans = 0
    for a, b in C:
        if M > b:
            M -= b
            ans += a * b
        else:
            ans += a * M
            break
    print(ans)
