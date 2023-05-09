def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            if P[i] == N - 1 or P[i] == 1:
                count += 1
        elif i == N - 1:
            if P[i] == N - 2 or P[i] == 0:
                count += 1
        else:
            if P[i] == P[i - 1] - 1 or P[i] == P[i - 1] + 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()