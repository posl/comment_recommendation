Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    if n == 1:
        for i in range(10):
            if i == 0:
                if 1 in s:
                    continue
                else:
                    print(0)
                    return
            if i == c[s.index(1)]:
                print(i)
                return
        print(-1)
        return
    if n == 2:
        for i in range(10):
            for j in range(10):
                if i == 0:
                    if 1 in s:
                        continue
                    else:
                        print(0)
                        return
                if j == 0:
                    if 2 in s:
                        continue
                    else:
                        print(0)
                        return
                if i == c[s.index(1)] and j == c[s.index(2)]:
                    print(i * 10 + j)
                    return
        print(-1)
        return
    if n == 3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == 0:
                        if 1 in s:
                            continue
                        else:
                            print(0)
                            return
                    if j == 0:
                        if 2 in s:
                            continue
                        else:
                            print(0)
                            return
                    if k == 0:
                        if 3 in s:
                            continue
                        else:
                            print(0)
                            return
                    if i == c[s.index(1)] and j == c[s.index(2)] and k == c[s.index(3)]:
                        print(i * 100 + j * 10 + k)
                        return
        print(-1)
        return

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = [0] * M
    C = [0] * M
    for i in range(M):
        S[i], C[i] = map(int, input().split())
    #print(N, M, S, C)
    ans = -1
    for i in range(10 ** (N - 1), 10 ** N):
        for j in range(M):
            if int(str(i)[S[j] - 1]) != C[j]:
                break
        else:
            ans = i
            break
    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    s = []
    c = []
    for i in range(m):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    if n == 1:
        for i in range(10):
            if i == c[0]:
                print(i)
                return
        print(-1)
        return
    if n == 2:
        for i in range(10):
            for j in range(10):
                if i == c[0] and j == c[1]:
                    print(str(i)+str(j))
                    return
        print(-1)
        return
    if n == 3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == c[0] and j == c[1] and k == c[2]:
                        print(str(i)+str(j)+str(k))
                        return
        print(-1)
        return

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    s = []
    c = []
    for i in range(M):
        s_i,c_i = map(int,input().split())
        s.append(s_i)
        c.append(c_i)
    for i in range(10**(N-1),10**N):
        for j in range(M):
            if str(i)[s[j]-1] != str(c[j]):
                break
        else:
            print(i)
            exit()
    print(-1)

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    sc = [list(map(int, input().split())) for i in range(m)]
    ans = -1
    for i in range(10**(n-1), 10**n):
        s = str(i)
        for j in range(m):
            if int(s[sc[j][0]-1]) != sc[j][1]:
                break
        else:
            ans = i
            break
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int, input().split())
    sc = []
    for i in range(m):
        s,c = map(int, input().split())
        sc.append([s,c])
    sc.sort(key=lambda x: x[0])
    ans = -1
    for i in range(10**(n-1), 10**n):
        i = str(i)
        if len(i) != n:
            continue
        for j in range(m):
            if i[sc[j][0]-1] != str(sc[j][1]):
                break
        else:
            ans = i
            break
    print(ans)

=======
Suggestion 7

def main():
    # input
    N, M = map(int, input().split())
    scs = []
    for i in range(M):
        scs.append(list(map(int, input().split())))
    # compute

    # output
    print(ans)

=======
Suggestion 8

def get_input():
    n, m = input().split()
    n = int(n)
    m = int(m)
    s = []
    c = []
    for i in range(m):
        s_i, c_i = input().split()
        s_i = int(s_i)
        c_i = int(c_i)
        s.append(s_i)
        c.append(c_i)
    return n, m, s, c

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #print(N, M)
    s = []
    c = []
    for i in range(M):
        s_i, c_i = map(int, input().split())
        s.append(s_i)
        c.append(c_i)
    #print(s, c)
    if N == 1:
        if M == 0:
            print(0)
        elif M == 1:
            print(c[0])
        else:
            print(-1)
    elif N == 2:
        if M == 0:
            print(10)
        elif M == 1:
            print(-1)
        else:
            if s[0] == 1 and c[0] == 0:
                print(-1)
            else:
                print("{}{}".format(c[0], c[1]))
    elif N == 3:
        if M == 0:
            print(100)
        elif M == 1:
            if s[0] == 1:
                print("{}0".format(c[0]))
            elif s[0] == 2:
                print("{}0".format(c[0]))
            elif s[0] == 3:
                print("0{}".format(c[0]))
            else:
                print(-1)
        elif M == 2:
            if s[0] == 1 and c[0] == 0 and s[1] == 2 and c[1] == 0:
                print(-1)
            elif s[0] == 1 and c[0] == 0 and s[1] == 3 and c[1] == 0:
                print(-1)
            elif s[0] == 2 and c[0] == 0 and s[1] == 3 and c[1] == 0:
                print(-1)
            elif s[0] == 1 and c[0] == 0 and s[1] == 2 and c[1] == 1:
                print(-1)
            elif s[0] == 1 and c[0] == 0 and s[1] == 3 and c[1] == 1:
                print(-1)
            elif s[0] == 2 and c[0] == 0 and s[1]

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    s_c = [list(map(int,input().split())) for _ in range(M)]
    ans = [-1]*N
    for i in range(M):
        if ans[s_c[i][0]-1] == -1:
            ans[s_c[i][0]-1] = s_c[i][1]
        else:
            if ans[s_c[i][0]-1] != s_c[i][1]:
                print(-1)
                exit()
    if N != 1 and ans[0] == 0:
        print(-1)
        exit()

    if N != 1 and ans[0] == -1:
        ans[0] = 1
    elif N != 1 and ans[0] == -1:
        ans[0] = 0

    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0
    print(*ans,sep="")

main()
