def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            count += 1
            min = P[i]
    print(count+1)

if __name__ == '__main__':
    main()