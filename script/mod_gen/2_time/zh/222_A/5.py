def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    
    #print(N)
    #print(A)
    #print(B)
    
    # 1. 计算每个玩家的登录时间
    # 2. 统计每天登录的玩家数目
    # 3. 统计每个玩家登录的天数
    # 4. 统计每个玩家登录的天数的玩家数目
    
    # 1. 计算每个玩家的登录时间
    login_time = []
    for i in range(N):
        login_time_i = []
        for j in range(B[i]):
            login_time_i.append(A[i] + j)
        login_time.append(login_time_i)
    
    #print(login_time)
    
    # 2. 统计每天登录的玩家数目
    login_times = []
    for i in range(N):
        for j in range(B[i]):
            login_times.append(A[i] + j)
    
    #print(login_times)
    
    login_times = sorted(login_times)
    
    #print(login_times)
    
    # 3. 统计每个玩家登录的天数
    login_days = []
    for i in range(N):
        login_days.append(B[i])
    
    #print(login_days)
    
    # 4. 统计每个玩家登录的天数的玩家数目
    login_days_num = []
    for i in range(N):
        login_days_num.append(login_days.count(login_days[i]))
    
    #print(login_days_num)
    
    # 5. 去除重复的登录天数
    login_days_num = list(set(login_days_num))
    
    #print(login_days_num)
    
    # 6. 统计每天登录的玩家数目
    login_times_num = []
    for i in range(len(login_days_num)):
        login_times_num.append(login_times.count(login_days_num[i]))
    
    #print(login_times_num)
    
    # 7. 输出
    for i in range(len(login_times_num)):
        if i

if __name__ == '__main__':
    main()