def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    #print(A)
    sum = 0
    for i in range(N):
        if i < L:
            sum += A[i]
        else:
            sum += A[L-1]
    print(sum)

if __name__ == '__main__':
    main()