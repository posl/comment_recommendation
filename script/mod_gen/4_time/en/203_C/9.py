def main():
    N, K = [int(v) for v in input().split()]
    AB = [[int(v) for v in input().split()] for _ in range(N)]
    AB.sort(key=lambda ab: ab[0])
    for ab in AB:
        if K < ab[0]:
            break
        K += ab[1]
    print(K)

if __name__ == '__main__':
    main()