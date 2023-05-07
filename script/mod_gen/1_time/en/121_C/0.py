def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    AB = sorted(zip(A, B))
    ans = 0
    for a, b in AB:
        if M <= b:
            ans += a * M
            break
        else:
            ans += a * b
            M -= b
    print(ans)

if __name__ == '__main__':
    main()