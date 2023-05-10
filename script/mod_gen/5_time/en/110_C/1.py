def main():
    s = input()
    t = input()
    s_list = list(s)
    t_list = list(t)
    s_list.sort()
    t_list.sort(reverse=True)
    s = ''.join(s_list)
    t = ''.join(t_list)
    if s < t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()