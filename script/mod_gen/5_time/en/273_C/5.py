def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = [0]*N
    for i in range(N):
        ans[i] = A[i]
    for i in range(N-2,-1,-1):
        if A[i] == A[i+1]:
            ans[i] = ans[i+1]
    for i in range(N):
        if i == 0:
            print(N-ans[i])
        else:
            print(N-ans[i]-i)

if __name__ == '__main__':
    main()