def main():
    N, K, X = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list.sort()
    total = 0
    for i in range(N - K):
        total += A_list[i]
    total += K * X
    print(total)

if __name__ == '__main__':
    main()