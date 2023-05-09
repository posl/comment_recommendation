def main():
    n, m = map(int, input().split())
    p_s_list = [input().split() for _ in range(m)]
    ac_list = [0] * n
    wa_list = [0] * n
    for p_s in p_s_list:
        if p_s[1] == 'AC':
            ac_list[int(p_s[0])-1] = 1
        else:
            if ac_list[int(p_s[0])-1] == 0:
                wa_list[int(p_s[0])-1] += 1
    print(sum(ac_list), sum([ac_list[i]*wa_list[i] for i in range(n)]))

if __name__ == '__main__':
    main()