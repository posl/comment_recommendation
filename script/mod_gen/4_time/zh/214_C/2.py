def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    time = [0 for i in range(N)]
    time[0] = T[0]
    for i in range(1, N):
        if T[i] <= time[i-1]:
            time[i] = time[i-1] + S[i]
        else:
            time[i] = T[i]
    for i in range(N):
        print(time[i])

if __name__ == '__main__':
    main()