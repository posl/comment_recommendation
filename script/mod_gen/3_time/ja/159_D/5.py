def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.append(0)
    count = 1
    ans = [0]*N
    for i in range(1,N+1):
        if A[i] == A[i-1]:
            count += 1
        else:
            ans[count-1] += 1
            count = 1
    for i in range(N):
        ans[i] = ans[i]*(ans[i]-1)//2
    for i in range(N-1):
        ans[i+1] += ans[i]
    for i in range(N):
        print(ans[N-i-1])

if __name__ == '__main__':
    main()