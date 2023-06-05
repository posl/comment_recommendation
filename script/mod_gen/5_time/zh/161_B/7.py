def problems161_b():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sumA = sum(A)
    for i in range(m):
        if A[i] < sumA/(4*m):
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    problems161_b()