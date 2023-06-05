def main():
    # 读入数据
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    # 检查是否有重复
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] and t[i] == t[j]:
                print("No")
                return
    # 检查是否有重名
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] or t[i] == t[j]:
                print("Yes")
                return
    print("No")
