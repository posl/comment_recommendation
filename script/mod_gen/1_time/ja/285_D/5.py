def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    s_set = set(s)
    t_set = set(t)
    if len(s_set) == len(t_set):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()