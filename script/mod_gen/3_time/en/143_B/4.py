def main():
    N = int(input())
    d = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        for j in range(i, N):
            sum += d[i] * d[j]
    print(int(sum / 2))

if __name__ == '__main__':
    main()