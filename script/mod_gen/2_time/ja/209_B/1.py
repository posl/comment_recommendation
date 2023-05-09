def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += A[i]
        else:
            ans += A[i] - 1
    if ans <= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()