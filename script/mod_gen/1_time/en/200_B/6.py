def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")
    print(N)
main()
Last modified: 2021-03-15 19:00:31 +0900

if __name__ == '__main__':
    main()