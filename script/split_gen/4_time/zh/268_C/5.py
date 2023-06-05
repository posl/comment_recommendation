def solve():
    N = int(input())
    p = list(map(int,input().split()))
    #print(N)
    #print(p)
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    if cnt == N:
        print(N)
    else:
        print(cnt + 2*(N-cnt)//3)
