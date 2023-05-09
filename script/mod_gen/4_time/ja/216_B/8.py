def problem216b():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_tmp, t_tmp = input().split()
        s.append(s_tmp)
        t.append(t_tmp)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    problem216b()