Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    num = -1
    for i in range(10**(N-1), 10**N):
        flag = True
        for j in range(M):
            if str(i)[s[j]-1] != str(c[j]):
                flag = False
        if flag:
            num = i
            break
    print(num)

=======
Suggestion 2

def solve(n, m, sc):
    if n == 1:
        if m == 1:
            return sc[0][1]
        else:
            return -1
    elif n == 2:
        if m == 1:
            return sc[0][1] * 10 + sc[1][1]
        elif m == 2:
            if sc[0][0] == 1:
                return sc[0][1] * 10 + sc[1][1]
            else:
                return sc[1][1] * 10 + sc[0][1]
        else:
            return -1
    else:
        if m == 1:
            return sc[0][1] * 100 + sc[0][1] * 10 + sc[0][1]
        elif m == 2:
            if sc[0][0] == 1:
                return sc[0][1] * 100 + sc[1][1] * 10 + sc[1][1]
            elif sc[1][0] == 1:
                return sc[1][1] * 100 + sc[0][1] * 10 + sc[0][1]
            else:
                return -1
        elif m == 3:
            if sc[0][0] == 1:
                if sc[1][0] == 2:
                    return sc[0][1] * 100 + sc[1][1] * 10 + sc[2][1]
                else:
                    return sc[0][1] * 100 + sc[2][1] * 10 + sc[1][1]
            elif sc[1][0] == 1:
                if sc[0][0] == 2:
                    return sc[1][1] * 100 + sc[0][1] * 10 + sc[2][1]
                else:
                    return sc[1][1] * 100 + sc[2][1] * 10 + sc[0][1]
            else:
                if sc[0][0] == 2:
                    return sc[2][1] * 100 + sc[0][1] * 10 + sc[1][1]
                else:
                    return sc[2][1] * 100 + sc

=======
Suggestion 3

def solve():
    n,m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    ans = -1
    for i in range(10**(n-1), 10**n):
        i = str(i)
        for s,c in sc:
            if i[s-1] != str(c): break
        else:
            ans = i
            break
    print(ans)

solve()

=======
Suggestion 4

def main():
    # 输入
    n, m = map(int, input().split())
    s = []
    c = []
    for i in range(m):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)

    # 求解
    # 1. 生成所有满足条件的数字
    # 2. 从小到大排序
    # 3. 输出第一个数字
    # 4. 如果没有满足条件的数字，输出-1
    if n == 1:
        print(c[0])
    elif n == 2:
        num = []
        for i in range(10):
            for j in range(10):
                if i == c[0] and j == c[1]:
                    num.append(i * 10 + j)
        if len(num) > 0:
            num.sort()
            print(num[0])
        else:
            print(-1)
    elif n == 3:
        num = []
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == c[0] and j == c[1] and k == c[2]:
                        num.append(i * 100 + j * 10 + k)
        if len(num) > 0:
            num.sort()
            print(num[0])
        else:
            print(-1)

=======
Suggestion 5

def get_num(n, m, s_c):
    if n == 1:
        if s_c[0][0] == 1:
            return s_c[0][1]
        else:
            return -1
    elif n == 2:
        if s_c[0][0] == 1 and s_c[1][0] == 2:
            return s_c[0][1]*10 + s_c[1][1]
        else:
            return -1
    else:
        if s_c[0][0] == 1 and s_c[1][0] == 2 and s_c[2][0] == 3:
            return s_c[0][1]*100 + s_c[1][1]*10 + s_c[2][1]
        else:
            return -1

=======
Suggestion 6

def problems157_c():
    pass

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    s = [0 for _ in range(M)]
    c = [0 for _ in range(M)]
    for i in range(M):
        s[i],c[i] = map(int,input().split())
    for i in range(10**(N-1),10**N):
        flag = True
        for j in range(M):
            if str(i)[s[j]-1] != str(c[j]):
                flag = False
                break
        if flag:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 8

def get_input():
    N, M = map(int, raw_input().split())
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, raw_input().split())
        s.append(s_i)
        c.append(c_i)
    return N, M, s, c

=======
Suggestion 9

def sol():
    n,m = map(int,input().split())
    s = []
    c = []
    for i in range(m):
        s_i,c_i = map(int,input().split())
        s.append(s_i)
        c.append(c_i)
    for i in range(10**(n-1),10**n):
        flag = True
        for j in range(m):
            if int(str(i)[s[j]-1]) != c[j]:
                flag = False
                break
        if flag:
            print(i)
            return
    print(-1)

=======
Suggestion 10

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
