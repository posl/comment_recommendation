def main():
    N,M = map(int, input().split())
    a = []
    for i in range(M):
        a.append(int(input()))
    a.append(N+1)
    d = [0]*(N+2)
    d[0] = 1
    for i in range(N+1):
        for j in range(M+1):
            if a[j] == i+1:
                break
            d[i+1] += d[i-j]
            d[i+1] %= 1000000007
    print(d[N])
main()

if __name__ == '__main__':
    main()