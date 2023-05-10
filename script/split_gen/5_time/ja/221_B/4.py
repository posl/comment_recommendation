def main():
    s = input()
    t = input()
    if s == t:
        print("Yes")
        return
    s_list = list(s)
    t_list = list(t)
    for i in range(len(s_list)-1):
        tmp = s_list[i]
        s_list[i] = s_list[i+1]
        s_list[i+1] = tmp
        if s_list == t_list:
            print("Yes")
            return
        tmp = s_list[i]
        s_list[i] = s_list[i+1]
        s_list[i+1] = tmp
    print("No")
    return
