def main():
    s = input()
    t = input()
    #s = 'chokudai'
    #t = 'Redder'
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort()
    if s_list == t_list:
        print('Yes')
    else:
        print('No')
