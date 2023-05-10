def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    T -= 1
    sum = 0
    for i in range(N):
        sum += A[i]
    cnt = T // sum
    T -= cnt * sum
    for i in range(N):
        T -= A[i]
        if T < 0:
            print(i+1, -T)
            return

if __name__ == '__main__':
    main()