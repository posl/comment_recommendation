def problem157_c():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    for i in range(10 ** (N-1), 10 ** N):
        i_str = str(i)
        for j in range(M):
            if i_str[s[j] - 1] != str(c[j]):
                break
        else:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    problem157_c()