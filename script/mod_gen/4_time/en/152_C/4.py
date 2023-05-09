def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = N + 1
    for i in range(0, N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count)

if __name__ == '__main__':
    main()