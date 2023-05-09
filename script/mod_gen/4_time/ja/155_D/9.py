def problem155_d():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    print(A)
    print(A[K])

if __name__ == '__main__':
    problem155_d()