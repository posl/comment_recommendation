def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    num = -1
    for i in range(10**(N-1),10**N):
        flag = True
        for j in range(M):
            if int(str(i)[s[j]-1]) != c[j]:
                flag = False
        if flag:
            num = i
            break
    print(num)
