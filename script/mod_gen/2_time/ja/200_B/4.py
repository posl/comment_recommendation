def main():
    N, K = map(int, input().split())
    for i in range(1, K+1):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")
    print(N)

if __name__ == '__main__':
    main()