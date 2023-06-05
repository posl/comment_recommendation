def main():
    #读取输入
    n = int(input())
    #存储输入
    s = []
    t = []
    for i in range(n):
        s_temp, t_temp = input().split()
        s.append(s_temp)
        t.append(t_temp)
    #判断是否有重复
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] or s[i] == t[j] or t[i] == s[j] or t[i] == t[j]:
                    print("No")
                    exit()
    print("Yes")
