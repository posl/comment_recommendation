def main():
    N,M,T = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    result = 'Yes'
    if A[0] > 0.5:
        result = 'No'
    if B[-1] < T-0.5:
        result = 'No'
    for i in range(M-1):
        if B[i] != A[i+1]:
            result = 'No'
    for i in range(M):
        if (B[i]-A[i]) % 2 == 0:
            result = 'No'
    for i in range(M-1):
        if A[i+1]-B[i] < 2:
            result = 'No'
    print(result)

if __name__ == '__main__':
    main()