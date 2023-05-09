def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    friend = [0] * N
    friend[X-1] = 1
    for i in range(N):
        if friend[A[i]-1] == 1:
            friend[A[i]-1] = 1
            friend[i] = 1
    print(sum(friend))

if __name__ == '__main__':
    main()