def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_P = N+1
    count = 0
    for i in range(N):
        if P[i] <= min_P:
            min_P = P[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()