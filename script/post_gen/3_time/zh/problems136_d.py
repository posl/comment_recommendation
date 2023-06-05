Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'L':
            ans[i-1] += (n-i) // 2 + 1
            ans[i] += (n-i) // 2
        else:
            ans[i] += (i+1) // 2
            ans[i-1] += (i+1) // 2 + 1
    print(' '.join(map(str, ans)))

=======
Suggestion 2

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
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i + 1] += (cnt + 1) // 2
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 3

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R':
            if i % 2 == 0:
                ans[i+1] += 1
            else:
                ans[i-1] += 1
        else:
            if i % 2 == 0:
                ans[i-1] += 1
            else:
                ans[i+1] += 1
    print(' '.join(map(str, ans)))

=======
Suggestion 4

def main():
    # 读入数据
    s = input()

    # 解决问题
    n = len(s)
    # 从左向右扫描，记录从左向右的第一个R的位置
    rpos = 0
    while rpos < n and s[rpos] != 'R':
        rpos += 1
    # 从左向右扫描，记录从右向左的第一个L的位置
    lpos = n - 1
    while lpos >= 0 and s[lpos] != 'L':
        lpos -= 1
    # 从左向右扫描，记录每个L的位置
    lpos_list = []
    for i in range(n):
        if s[i] == 'L':
            lpos_list.append(i)
    # 从右向左扫描，记录每个R的位置
    rpos_list = []
    for i in range(n - 1, -1, -1):
        if s[i] == 'R':
            rpos_list.append(i)
    # 计算每个孩子的位置
    pos = [0] * n
    for i in range(len(lpos_list)):
        pos[lpos_list[i]] = i + 1
    for i in range(len(rpos_list)):
        pos[rpos_list[i]] = i + 1
    # 计算每个孩子的移动次数
    move = [0] * n
    for i in range(len(lpos_list)):
        move[lpos_list[i]] = lpos_list[i] - rpos_list[i] - 1
    for i in range(len(rpos_list)):
        move[rpos_list[i]] = rpos_list[i] - lpos_list[i] - 1
    # 计算每个孩子的最终位置
    final_pos = [0] * n
    for i in range(n):
        final_pos[i] = pos[i] + move[i]
    # 计算每个孩子的最终位置上站的孩子的数量
    ans = [0] * n
    for i in range(n):
        ans[final_pos[i] - 1] += 1

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    r = [0] * n
    l = [0] * n
    r_count = 0
    l_count = 0
    for i in range(n):
        if s[i] == 'R':
            r_count += 1
        else:
            r_count = 0
        r[i] = r_count
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            l_count += 1
        else:
            l_count = 0
        l[i] = l_count
    for i in range(n):
        if s[i] == 'R' and s[i+1] == 'L':
            r[i] += 1
            l[i+1] += 1
    for i in range(n):
        print(r[i]+l[i], end=' ')
    print()

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    ans = [0] * n
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
    print(' '.join(map(str, ans)))

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    i = 0
    while i < n - 1:
        if s[i] == "R":
            j = i
            while j < n - 1 and s[j] == "R":
                j += 1
            if (j - i) % 2 == 0:
                ans[j] += 1
            else:
                ans[j - 1] += 1
        i += 1
    i = n - 1
    while i > 0:
        if s[i] == "L":
            j = i
            while j > 0 and s[j] == "L":
                j -= 1
            if (i - j) % 2 == 0:
                ans[j] += 1
            else:
                ans[j + 1] += 1
        i -= 1
    print(" ".join(map(str, ans)))

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    a = [0]*n
    for i in range(n):
        a[i] = 1
    for i in range(n):
        if s[i] == 'R':
            a[i+1] += a[i]
            a[i] = 0
    for i in range(n-1, -1, -1):
        if s[i] == 'L':
            a[i-1] += a[i]
            a[i] = 0
    for i in range(n):
        print(a[i], end=' ')
    print()

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    l = [0] * n
    r = [0] * n
    for i in range(1, n):
        if s[i] == 'L':
            l[i] = l[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if s[i] == 'R':
            r[i] = r[i + 1] + 1
    for i in range(n):
        print(l[i] + r[i] + 1, end=' ')
    print()

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        if S[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i-1] += (cnt + 1) // 2
            cnt = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += (cnt + 1) // 2
            cnt = 0
    print(' '.join(map(str, ans)))
