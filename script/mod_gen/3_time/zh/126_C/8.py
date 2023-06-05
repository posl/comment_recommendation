def main():
    N, K = map(int, input().split())
    prob = 0
    for i in range(1, N + 1):
        if i >= K:
            prob += 1 / N
        else:
            prob += (1 / N) * (1 / 2) ** (len(bin(K - 1 - i)) - 2)
    print(prob)

if __name__ == '__main__':
    main()