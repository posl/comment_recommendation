def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    B = [0] + [0] * (2 * 10 ** 5) + [0]
    for i in range(N // 2):
        a = A[i + 1]
        b = A[N - i]
        if a == b:
            continue
        if a > b:
            a, b = b, a
        if B[a] == b:
            continue
        if B[a] > 0:
            print(-1)
            return
        B[a] = b
    ans = 0
    for i in range(1, 2 * 10 ** 5 + 1):
        if B[i] > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()