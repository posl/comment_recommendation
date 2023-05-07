def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N + 1]
    d = [A[i + 1] - A[i] - 1 for i in range(M + 1)]
    d.sort(reverse=True)
    k = d[0]
    if k == 0:
        print(0)
        return
    ans = 0
    for i in range(M + 1):
        if d[i] == 0:
            break
        ans += (d[i] + k - 1) // k
    print(ans)

if __name__ == '__main__':
    main()