def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    print(S)
    print(T)
    time = [0] * N
    for i in range(N):
        time[i] = T[i]
    for i in range(N):
        if time[i] > time[i - 1] + S[i - 1]:
            time[i] = time[i - 1] + S[i - 1]
    for i in range(N):
        print(time[i])

if __name__ == '__main__':
    main()