Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    i = 0
    while i < n:
        j = i
        while j < n and s[j] == 'R':
            j += 1
        k = j
        while k < n and s[k] == 'L':
            k += 1
        if (j - i) % 2 == 0:
            ans[j - 1] += (j - i) // 2
            ans[j] += (j - i) // 2
        else:
            if (j - i) % 2 == 1:
                ans[j - 1] += (j - i) // 2 + 1
                ans[j] += (j - i) // 2
        i = k
    print(*ans)

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    #print(ans)
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
            if i == n - 1:
                ans[i] += cnt
        else:
            ans[i] += cnt
            cnt = 0
    #print(ans)
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            cnt += 1
            if i == 0:
                ans[i] += cnt
        else:
            ans[i] += cnt
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 3

def main():
    # 读入数据
    S = input()
    # print(S)
    # 初始化
    # 从左到右的方向
    left_to_right = True
    # 记录每个方格上的小孩数
    child_count = [1]*len(S)
    # print(child_count)
    # 按照方向进行移动
    for i in range(100):
        # print(i)
        # print(child_count)
        # print(left_to_right)
        # print(S)
        # print()
        # 移动
        if left_to_right:
            # 从左到右移动
            for j in range(len(S)-1):
                if S[j] == 'R' and S[j+1] == 'L':
                    child_count[j] += child_count[j+1]
                    child_count[j+1] = 0
            left_to_right = False
        else:
            # 从右到左移动
            for j in range(len(S)-1,0,-1):
                if S[j] == 'L' and S[j-1] == 'R':
                    child_count[j] += child_count[j-1]
                    child_count[j-1] = 0
            left_to_right = True
    # 输出
    print(' '.join(map(str, child_count)))

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'R' and s[i + 1] == 'L':
            r = i
            l = i + 1
            while s[r] == 'R':
                r -= 1
            while s[l] == 'L':
                l += 1
            if (r - i) % 2 == 0 and (i - l) % 2 == 0:
                ans[i] += 1
            elif (r - i) % 2 != 0 and (i - l) % 2 != 0:
                ans[i + 1] += 1
            elif (r - i) % 2 == 0 and (i - l) % 2 != 0:
                ans[i] += 1
                ans[i + 1] += 1
            elif (r - i) % 2 != 0 and (i - l) % 2 == 0:
                ans[i] += 1
                ans[i + 1] += 1
    print(*ans)

=======
Suggestion 5

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
            ans[i-1] += cnt - cnt // 2
            cnt = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += cnt - cnt // 2
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    #print(s)
    #print(n)
    #print(s[0])
    #print(s[n-1])
    #print(s[0] == 'R')
    #print(s[n-1] == 'L')
    if s[0] == 'R' and s[n-1] == 'L':
        s = s + 'R'
        #print(s)
        n = n + 1
        #print(n)
        a = [0] * n
        #print(a)
        i = 0
        while i < n:
            if s[i] == 'R':
                j = i + 1
                while s[j] == 'R':
                    j += 1
                #print(j)
                j -= 1
                #print(j)
                if (j - i) % 2 == 0:
                    a[j] += 1
                else:
                    a[j - 1] += 1
                i = j + 1
            else:
                j = i - 1
                while s[j] == 'L':
                    j -= 1
                #print(j)
                j += 1
                #print(j)
                if (i - j) % 2 == 0:
                    a[j] += 1
                else:
                    a[j + 1] += 1
                i = j + 1
        #print(a)
        for i in range(n):
            print(a[i], end = ' ')
        print()
    else:
        print('Error!')

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    i = 0
    while i < n:
        if s[i] == 'L':
            #找到第一个R
            j = i
            while j < n and s[j] == 'L':
                j += 1
            #j是第一个R的位置
            #找到第一个L
            k = j
            while k < n and s[k] == 'R':
                k += 1
            #k是第一个L的位置
            #偶数个
            if (k - j) % 2 == 0:
                ans[j-1] += (k-j)//2
                ans[j] += (k-j)//2
            #奇数个
            else:
                ans[j-1] += (k-j+1)//2
                ans[j] += (k-j-1)//2
            i = k
        else:
            #找到第一个L
            j = i
            while j < n and s[j] == 'R':
                j += 1
            #j是第一个L的位置
            #找到第一个R
            k = j
            while k < n and s[k] == 'L':
                k += 1
            #k是第一个R的位置
            #偶数个
            if (k - j) % 2 == 0:
                ans[j-1] += (k-j)//2
                ans[j] += (k-j)//2
            #奇数个
            else:
                ans[j-1] += (k-j-1)//2
                ans[j] += (k-j+1)//2
            i = k
    print(*ans)

=======
Suggestion 8

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    for i in range(n):
        if s[i] == 'R':
            if i+1 < n and s[i+1] == 'R':
                ans[i+2] += ans[i]
                ans[i] = 0
            else:
                ans[i+1] += ans[i] + 1
                ans[i] = 0
        else:
            ans[i-1] += ans[i]
            ans[i] = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    r = 0
    l = 0
    for i in range(n):
        if s[i] == 'R':
            r = i
        else:
            l = i
        if s[i] == 'R' and s[i + 1] == 'L':
            ans[r] += (i + 1 - r) // 2
            ans[l] += (i + 1 - r + 1) // 2
            r = i + 1
    for i in range(n):
        print(ans[i], end=' ')

=======
Suggestion 10

def main():
    pass
