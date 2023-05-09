def main():
    N, K = map(int, input().split())
    sweets = [0] * N
    for _ in range(K):
        for a in map(int, input().split()[1:]):
            sweets[a - 1] += 1
    print(sweets.count(0))

if __name__ == '__main__':
    main()