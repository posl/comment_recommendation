def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    s_set = set(s_list)
    t_set = set(t_list)
    if len(s_set) != len(t_set):
        print("No")
        return
    else:
        s_dict = {}
        t_dict = {}
        for i in range(len(s_set)):
            s_dict[s_set.pop()] = 0
            t_dict[t_set.pop()] = 0
        for i in range(len(s)):
            s_dict[s_list[i]] += 1
            t_dict[t_list[i]] += 1
        if s_dict == t_dict:
            print("Yes")
        else:
            print("No")
        return
