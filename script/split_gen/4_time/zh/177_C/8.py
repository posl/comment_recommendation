def main():
    # input
    N = int(input())
    A = list(map(int,input().split()))
    # calculate
    sum = 0
    for i in range(N-1):
        for j in range(i+1,N):
            sum = sum + A[i]*A[j]
    # print
    print(sum%(10**9+7))
main()
