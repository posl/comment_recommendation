def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

if __name__ == '__main__':
    main()