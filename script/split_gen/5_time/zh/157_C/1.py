def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(N, M, s, c)
    for i in range(10**(N-1), 10**N):
        i_str = str(i)
        flag = True
        for j in range(M):
            if i_str[s[j]-1] != str(c[j]):
                flag = False
                break
        if flag:
            print(i)
            break
    else:
        print(-1)
