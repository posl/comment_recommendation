def main():
    #input
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    #output
    print(*[A[i-1]+L[j]-1 for j,i in enumerate(L)])

if __name__ == '__main__':
    main()