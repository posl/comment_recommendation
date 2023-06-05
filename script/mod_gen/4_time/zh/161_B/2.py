def problems161_b():
    n,m = input().split()
    n = int(n)
    m = int(m)
    A = input().split()
    A = list(map(int,A))
    A.sort(reverse=True)
    total = sum(A)
    for i in range(m):
        if A[i] < total/(4*m):
            print("否")
            return
    print("是")
    return

if __name__ == '__main__':
    problems161_b()