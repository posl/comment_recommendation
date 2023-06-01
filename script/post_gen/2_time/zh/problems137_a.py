Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += (cnt + 1) // 2
            cnt = 0
    print(*ans)

=======
Suggestion 2

def main():
    s = input()
    l = len(s)
    #print(l)
    #print(s)
    #print(s[0])
    #print(s[l-1])
    #print(s[0] == 'R')
    #print(s[l-1] == 'L')
    if s[0] == 'R' and s[l-1] == 'L':
        for i in range(l):
            if s[i] == 'L' and s[i-1] == 'R':
                t = i
                break
        for i in range(l):
            if s[i] == 'L' and s[i+1] == 'R':
                t1 = i
                break
        #print(t)
        #print(t1)
        for i in range(l):
            if i < t:
                if (t - i) % 2 == 0:
                    print(0, end = ' ')
                else:
                    print(1, end = ' ')
            elif i == t:
                print(1, end = ' ')
            elif i > t and i < t1:
                print(2, end = ' ')
            elif i == t1:
                print(1, end = ' ')
            elif i > t1:
                if (i - t1) % 2 == 0:
                    print(1, end = ' ')
                else:
                    print(0, end = ' ')
    elif s[0] == 'R' and s[l-1] == 'R':
        for i in range(l):
            if s[i] == 'L' and s[i-1] == 'R':
                t = i
                break
        for i in range(l):
            if s[i] == 'L' and s[i+1] == 'R':
                t1 = i
                break
        #print(t)
        #print(t1)
        for i in range(l):
            if i < t:
                if (t - i) % 2 == 0:
                    print(0, end = ' ')
                else:
                    print(1, end = ' ')
            elif i == t:
                print(1, end = ' ')
            elif i > t and i < t1:
                print(2, end = ' ')
            elif i == t1:
                print(1, end =

=======
Suggestion 3

def main():
    # 读入数据
    S = input()
    N = len(S)
    # 初始化
    res = [0] * N
    for i in range(N):
        res[i] = 1
    # 模拟移动
    for i in range(10 ** 100):
        for j in range(N):
            if S[j] == 'R':
                # R向右走
                res[j + 1] += res[j]
                res[j] = 0
            else:
                # L向左走
                res[j - 1] += res[j]
                res[j] = 0
    # 输出结果
    print(' '.join(map(str, res)))

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    for i in range(n):
        if s[i] == 'R':
            ans[i+1] += 1
        else:
            ans[i] += 1
    for i in range(10**100):
        for j in range(n):
            if s[j] == 'R':
                ans[j+1] += 1
            else:
                ans[j] += 1
    print(*ans)

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    result = [0] * n
    for i in range(n):
        if s[i] == 'R' and s[i+1] == 'L':
            result[i] += 1
            result[i+1] += 1
            i += 2
        elif s[i] == 'R':
            result[i] += 1
            i += 1
        elif s[i] == 'L' and s[i-1] == 'R':
            result[i-1] += 1
            result[i] += 1
            i += 2
        elif s[i] == 'L':
            result[i] += 1
            i += 1
    print(result)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == "L":
            l = i
        if s[i] == "R":
            r = i
    for i in range(n):
        if s[i] == "R":
            if (r-i)%2 == 0:
                ans[r] += 1
            else:
                ans[r+1] += 1
        if s[i] == "L":
            if (i-l)%2 == 0:
                ans[l] += 1
            else:
                ans[l-1] += 1
    print(*ans)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i-1] += cnt - cnt // 2
            cnt = 0
    cnt = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += cnt - cnt // 2
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    pos = 0
    while pos < n:
        if s[pos] == 'R':
            pos += 1
        else:
            l = pos
            while pos < n and s[pos] == 'L':
                pos += 1
            r = pos
            if (r - l) % 2 == 0:
                ans[l] = (r - l) // 2
                ans[r - 1] = (r - l) // 2
            else:
                ans[l] = (r - l) // 2 + 1
                ans[r - 1] = (r - l) // 2
    print(" ".join(map(str, ans)))

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = [0] * n

    for i in range(n):
        if s[i] == 'R':
            j = i
            while j < n and s[j] == 'R':
                j += 1
            if (j - i) % 2 == 0:
                ans[j] += 1
            else:
                ans[j-1] += 1
        else:
            j = i
            while j >= 0 and s[j] == 'L':
                j -= 1
            if (i - j) % 2 == 0:
                ans[j] += 1
            else:
                ans[j+1] += 1

    print(' '.join(map(str, ans)))

=======
Suggestion 10

def solve():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            if s[i+1] == 'R':
                j = i
                while s[j] != 'L':
                    ans[j] += 1
                    j += 1
                if (j-i) % 2 == 1:
                    ans[j] += 1
            else:
                j = i
                while s[j] != 'L':
                    ans[j] += 1
                    j += 1
        else:
            if s[i-1] == 'L':
                j = i
                while s[j] != 'R':
                    ans[j] += 1
                    j -= 1
                if (i-j) % 2 == 1:
                    ans[j] += 1
            else:
                j = i
                while s[j] != 'R':
                    ans[j] += 1
                    j -= 1
    print(' '.join(map(str, ans)))

solve()
