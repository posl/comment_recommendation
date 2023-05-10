Synthesizing 10/10 solutions

=======
Suggestion 1

def check(n, s, c):
    for i in range(len(s)):
        if n[s[i]-1] != c[i]:
            return False
    return True

n, m = map(int, input().split())
s = []
c = []
for _ in range(m):
    _s, _c = map(int, input().split())
    s.append(_s)
    c.append(_c)

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
        s[i] -= 1

    for i in range(10 ** n):
        str_i = str(i)
        if len(str_i) != n:
            continue
        for j in range(m):
            if str_i[s[j]] != str(c[j]):
                break
        else:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]

    ans = -1
    for i in range(10 ** n):
        si = str(i)
        if len(si) != n:
            continue
        flag = True
        for s, c in sc:
            if si[s - 1] != str(c):
                flag = False
                break
        if flag:
            ans = i
            break
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    for s, c in sc:
        if ans[s-1] != -1 and ans[s-1] != c:
            print(-1)
            exit()
        ans[s-1] = c
    if N > 1 and ans[0] == 0:
        print(-1)
        exit()
    if N > 1 and ans[0] == -1:
        ans[0] = 1
    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0
    print("".join(map(str, ans)))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    if n == 1:
        if m == 0:
            print(0)
        elif m == 1:
            print(c[0])
        else:
            print(-1)
    elif n == 2:
        if m == 0:
            print(0)
        elif m == 1:
            print(-1)
        elif m == 2:
            if s[0] == 1:
                print(-1)
            else:
                print(c[0] * 10 + c[1])
        else:
            print(-1)
    else:
        if m == 0:
            print(0)
        elif m == 1:
            print(-1)
        elif m == 2:
            print(-1)
        elif m == 3:
            if s[0] == 1:
                if s[1] == 2:
                    if s[2] == 3:
                        print(c[0] * 100 + c[1] * 10 + c[2])
                    else:
                        print(-1)
                elif s[1] == 3:
                    if s[2] == 2:
                        print(c[0] * 100 + c[2] * 10 + c[1])
                    else:
                        print(-1)
                else:
                    print(-1)
            elif s[0] == 2:
                if s[1] == 1:
                    if s[2] == 3:
                        print(c[1] * 100 + c[0] * 10 + c[2])
                    else:
                        print(-1)
                elif s[1] == 3:
                    if s[2] == 1:
                        print(c[1] * 100 + c[2] * 10 + c[0])
                    else:
                        print(-1)
                else:
                    print(-1)
            elif s[0] == 3:
                if s[1] == 1:
                    if s[2] == 2:
                        print(c[2] * 100 + c[0] *

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    for i in range(M):
        s, c = sc[i]
        if ans[s - 1] == -1 or ans[s - 1] == c:
            ans[s - 1] = c
        else:
            print(-1)
            exit(0)
    if N != 1 and ans[0] == 0:
        print(-1)
        exit(0)
    if N == 1 and ans[0] == -1:
        print(0)
        exit(0)
    if N == 1 and ans[0] != -1:
        print(ans[0])
        exit(0)
    if ans[0] == 0:
        print(-1)
        exit(0)
    for i in range(N):
        if ans[i] == -1:
            ans[i] = 0
    print(''.join(list(map(str, ans))))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    for i in range(10 ** n):
        s = str(i)
        if len(s) != n:
            continue
        for j in range(m):
            if int(s[sc[j][0] - 1]) != sc[j][1]:
                break
        else:
            print(i)
            exit()
    print(-1)

=======
Suggestion 8

def check(N, M, s, c):
    for i in range(M):
        if N < s[i]:
            return False
        if N == s[i] and c[i] != 0:
            return False
    return True

N, M = map(int, input().split())
s = []
c = []
for i in range(M):
    s_i, c_i = map(int, input().split())
    s.append(s_i)
    c.append(c_i)

for i in range(10 ** (N - 1), 10 ** N):
    if check(str(i), M, s, c):
        print(i)
        exit()
print(-1)

=======
Suggestion 9

def main():
    # データ入力
    n, m = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(m)]
    # 1桁の場合
    if n == 1:
        for i in range(10):
            if i == sc[0][0] and i == sc[0][1]:
                print(i)
                exit()
        print(-1)
        exit()
    # 2桁以上の場合
    for i in range(10**(n-1), 10**n):
        # 桁数チェック
        if len(str(i)) != n:
            continue
        # 条件チェック
        for j in range(m):
            if int(str(i)[sc[j][0]-1]) != sc[j][1]:
                break
            if j == m-1:
                print(i)
                exit()
    print(-1)

=======
Suggestion 10

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
