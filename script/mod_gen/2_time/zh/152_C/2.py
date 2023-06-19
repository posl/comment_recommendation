def main():
    N = int(input())
    P = list(map(int, input().split()))
    min_num = P[0]
    count = 1
    for i in range(1, N):
        if P[i] <= min_num:
            count += 1
            min_num = P[i]
    print(count)

if __name__ == '__main__':
    main()