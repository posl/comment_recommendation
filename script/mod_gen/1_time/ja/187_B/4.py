def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if y[i] - y[j] >= x[i] - x[j] and y[i] - y[j] <= x[i] - x[j]:
                count += 1
    print(count)
main()

if __name__ == '__main__':
    main()