def solve():
    N,X = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    #print(AB)
    #print(N,X)
    min_time = 10**9*N
    for i in range(N):
        time = 0
        for j in range(N):
            if j <= i:
                time += AB[j][0] + AB[j][1]
            else:
                time += AB[j][1]
        #print(time)
        min_time = min(min_time,time)
    print(min_time+X)

if __name__ == '__main__':
    solve()