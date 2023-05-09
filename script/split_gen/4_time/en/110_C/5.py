def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if len(s) == 1:
        if s == t:
            print("Yes")
        else:
            print("No")
        return
    s_list = sorted(list(s))
    t_list = sorted(list(t))
    s_list = [s_list[i] for i in range(len(s_list)) if i == 0 or s_list[i] != s_list[i-1]]
    t_list = [t_list[i] for i in range(len(t_list)) if i == 0 or t_list[i] != t_list[i-1]]
    if len(s_list) == len(t_list):
        print("Yes")
    else:
        print("No")
