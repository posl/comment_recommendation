def main():
    #input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    #output
    for i in range(N):
        if A[i] != X:
            print(A[i], end = ' ')
    print()

if __name__ == '__main__':
    main()