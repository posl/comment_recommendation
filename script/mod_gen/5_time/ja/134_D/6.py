def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N-1, -1, -1):
        #print(i)
        #print(B)
        cnt = 0
        for j in range(i+1, N+1, i+1):
            #print(j)
            cnt += B[j-1]
        #print(cnt)
        if cnt % 2 != A[i]:
            B[i] = 1
    ans = []
    for i in range(N):
        if B[i] == 1:
            ans.append(i+1)
    print(len(ans))
    if len(ans) > 0:
        print(*ans)

if __name__ == '__main__':
    main()