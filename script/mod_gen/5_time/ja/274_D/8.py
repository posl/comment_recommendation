def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    if A[0] > x or A[N-1] > y:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()