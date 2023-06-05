def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #print(A)
    #print(A[0], A[A[0]-1])
    i = 0
    k = 0
    while True:
        i = A[i] - 1
        k += 1
        if i == 0:
            break
        if k == K:
            break
    print(i+1)

if __name__ == '__main__':
    main()