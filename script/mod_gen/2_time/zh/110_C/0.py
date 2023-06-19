def main():
    S = input()
    T = input()
    s = S
    t = T
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list != t_list:
        print("No")
        return
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list)):
        for j in range(i+1,len(s_list)):
            s_list[i],s_list[j] = s_list[j],s_list[i]
            if s_list == t_list:
                print("Yes")
                return
            s_list[i],s_list[j] = s_list[j],s_list[i]
    print("No")

if __name__ == '__main__':
    main()