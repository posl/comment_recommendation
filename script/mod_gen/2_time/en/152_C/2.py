def main():
    N = int(input())
    P = list(map(int, input().split()))
    minval = P[0]
    count = 1
    for i in range(1, N):
        if minval >= P[i]:
            minval = P[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()