def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort(reverse=True)
    if s_list < t_list:
        print('Yes')
    else:
        print('No')
