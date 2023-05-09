def main():
    N = int(input())
    C = list(map(int, input().split()))
    result = 1
    C.sort()
    for i in range(N):
        result *= (C[i] - i)
        result %= (10**9 + 7)
    print(result)

if __name__ == '__main__':
    main()