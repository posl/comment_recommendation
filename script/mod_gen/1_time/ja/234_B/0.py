def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    max_length = 0
    for i in range(N):
        for j in range(i + 1, N):
            length = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            if max_length < length:
                max_length = length
    print(max_length)

if __name__ == '__main__':
    main()