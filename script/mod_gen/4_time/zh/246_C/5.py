def main():
    #N,K,X = map(int,input().split())
    #A = list(map(int,input().split()))
    #print(N,K,X)
    #print(A)
    N,K,X = 20,815,60
    A = [2066, 3193, 2325, 4030, 3725, 1669, 1969, 763, 1653, 159, 5311, 5341, 4671, 2374, 4513, 285, 810, 742, 2981, 202]
    A.sort()
    sum = 0
    for i in range(N):
        if K>0:
            if A[i]>=X:
                sum += A[i]-X
                K -= 1
            else:
                sum += A[i]
        else:
            sum += A[i]
    print(sum)

if __name__ == '__main__':
    main()