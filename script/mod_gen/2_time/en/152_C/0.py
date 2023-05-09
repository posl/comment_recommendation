def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 1
    min = P[0]
    for i in range(1, N):
        if P[i] < min:
            min = P[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()