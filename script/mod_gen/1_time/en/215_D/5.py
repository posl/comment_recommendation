def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
    if M < gcd:
        print(0)
        return
    ans = []
    for i in range(1, int(math.sqrt(M)) + 1):
        if M % i == 0:
            if i % gcd == 1:
                ans.append(i)
            if i != M // i and (M // i) % gcd == 1:
                ans.append(M // i)
    ans.sort()
    print(len(ans))
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()