def main():
    N = int(input())
    #print(N)
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    d = {}
    for i in range(N):
        for j in range(A[i], A[i]+B[i]):
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    #print(d)
    for i in range(1, N+1):
        if i in d:
            print(d[i], end=" ")
        else:
            print(0, end=" ")
main()

if __name__ == '__main__':
    main()