def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.append(0)
    ans = 0
    cnt = 1
    for i in range(N):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans += cnt*(cnt-1)*(cnt-2)//6
            cnt = 1
    print(ans)
