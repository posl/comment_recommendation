def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    minP = 10**6
    for i in range(N):
        if P[i] < minP:
            count += 1
            minP = P[i]
    print(count)

if __name__ == '__main__':
    main()