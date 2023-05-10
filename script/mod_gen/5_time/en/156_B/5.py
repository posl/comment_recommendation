def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    count = 0
    while N > 0:
        N = N // K
        count += 1
    print(count)

if __name__ == '__main__':
    main()