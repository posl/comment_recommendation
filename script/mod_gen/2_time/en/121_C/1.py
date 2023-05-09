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
        if b <= M:
            ans += a * b
            M -= b
        else:
            ans += a * M
            break
    print(ans)

if __name__ == '__main__':
    main()