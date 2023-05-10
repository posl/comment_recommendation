def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    while N > K:
        N -= (K-1)
        count += 1
    print(count+1)

if __name__ == '__main__':
    main()