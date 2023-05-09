def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = N
    for i in range(N):
        if P[i] < min:
            count += 1
            min = P[i]
    print(count)

if __name__ == '__main__':
    main()