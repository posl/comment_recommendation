def main():
    #input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #compute
    for i in range(N):
        if i % 2 == 1:
            A[i] -= 1
    #output
    if sum(A) > X:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()