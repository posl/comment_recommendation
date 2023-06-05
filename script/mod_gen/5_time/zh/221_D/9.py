def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #计算每个玩家的登录日
    login_days = []
    for i in range(N):
        login_days.append([A[i], A[i]+B[i]-1])
    #print(login_days)
    #将登录日按照登录日的开始时间排序
    login_days.sort()
    #print(login_days)
    #计算每个玩家的登录日是否有重叠
    overlap = []
    for i in range(N-1):
        if login_days[i][1] >= login_days[i+1][0]:
            overlap.append([login_days[i][1], login_days[i+1][0]])
    #print(overlap)
    #计算每个玩家的登录日是否有重叠
    #count = 0
    #for i in range(N-1):
    #    if login_days[i][1] >= login_days[i+1][0]:
    #        count += 1
    #print(count)
    #计算每个玩家的登录日是否有重叠
    count = 0
    for i in range(len(overlap)-1):
        if overlap[i][0] >= overlap[i+1][1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()