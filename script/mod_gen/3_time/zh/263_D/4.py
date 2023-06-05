def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    min = 0
    for i in range(N):
        if A[i] > 0:
            min += A[i]
        else:
            min -= A[i]
    print(min)
    min = 0
    for i in range(N):
        if A[i] < 0:
            min += A[i]
        else:
            min += A[i]
    print(min)

if __name__ == '__main__':
    main()