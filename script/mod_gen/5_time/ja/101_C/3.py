def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    while N > 0:
        N -= K - 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()