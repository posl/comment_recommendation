def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i == N-1:
            break
        if A[i] + A[i+1] == abs(x-y):
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()