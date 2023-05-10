def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    #print(A)
    sum = 0
    for i in range(N):
        sum += A[i]
    #print(sum)
    for i in range(M):
        if A[i] < sum/(4*M):
            print("No")
            exit()
    print("Yes")

if __name__ == '__main__':
    main()