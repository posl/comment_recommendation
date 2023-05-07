def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        if i % 2 == 1:
            A[i] = max(0, A[i] - 1)
    if sum(A) <= X:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()