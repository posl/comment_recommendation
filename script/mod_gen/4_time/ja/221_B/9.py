def check(s,t):
    if s == t:
        print('Yes')
        return
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s)-1):
        s_list[i],s_list[i+1] = s_list[i+1],s_list[i]
        if s_list == t_list:
            print('Yes')
            return
        s_list[i],s_list[i+1] = s_list[i+1],s_list[i]
    print('No')
    return

if __name__ == '__main__':
    check()