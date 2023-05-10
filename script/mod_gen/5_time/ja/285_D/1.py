def main():
    n = int(input())
    s_t_list = [input().split() for _ in range(n)]
    for i in range(n):
        s_t_list[i].append(i)
    s_t_list = sorted(s_t_list, key=lambda x: x[0])
    s_list = [i[0] for i in s_t_list]
    t_list = [i[1] for i in s_t_list]
    index_list = [i[2] for i in s_t_list]
    for i in range(n-1):
        if t_list[i] == s_list[i+1]:
            continue
        else:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()