def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_value = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            values = V[:i] + V[N-j:]
            values.sort()
            value = sum(values)
            for k in range(min(K-i-j, len(values))):
                if values[k] < 0:
                    value -= values[k]
            max_value = max(max_value, value)
    print(max_value)

if __name__ == '__main__':
    main()