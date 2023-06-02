Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n - 1):
        if s[i] == "R" and s[i + 1] == "L":
            ans[i] += 1
            ans[i + 1] += 1
    for i in range(n):
        if s[i] == "R":
            if ans[i] % 2 == 1:
                ans[i + 1] += 1
            ans[i] //= 2
        else:
            if ans[i] % 2 == 1:
                ans[i - 1] += 1
            ans[i] //= 2
    print(*ans)

main()

=======
Suggestion 2

def main():
    # 读入数据
    S = input()
    # 处理数据
    N = len(S)
    # 从左向右计算
    R = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if i == 0:
                R[i] = 1
            else:
                R[i] = R[i-1] + 1
        else:
            R[i] = 0
    # 从右向左计算
    L = [0] * N
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            if i == N-1:
                L[i] = 1
            else:
                L[i] = L[i+1] + 1
        else:
            L[i] = 0
    # 计算结果
    result = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if i+L[i] < N:
                result[i+L[i]] += 1
            else:
                result[N-1] += 1
        else:
            if i-R[i] >= 0:
                result[i-R[i]] += 1
            else:
                result[0] += 1
    # 输出结果
    print(" ".join(map(str, result)))

=======
Suggestion 3

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
            ans[i-1] += (cnt+1) // 2
            cnt = 0
    cnt = 0
    for i in range(N-1, -1, -1):
        if S[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i+1] += (cnt+1) // 2
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 4

def countRL(s):
    r = 0
    l = 0
    for c in s:
        if c == 'R':
            r += 1
        else:
            l += 1
    return r, l

=======
Suggestion 5

def solve():
    s = input()
    n = len(s)
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i - 1] += cnt // 2
            if cnt % 2 == 1:
                ans[i - 1] += 1
            cnt = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2
            ans[i + 1] += cnt // 2
            if cnt % 2 == 1:
                ans[i + 1] += 1
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def problem136_d():
    s = input()
    n = len(s)
    ans = [0]*n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i-1] += (cnt+1)//2
            cnt = 0
    cnt = 0
    for i in range(n-1,-1,-1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt//2
            ans[i+1] += (cnt+1)//2
            cnt = 0
    print(' '.join(map(str,ans)))

problem136_d()

=======
Suggestion 7

def main():
    s = input()
    s = s.replace("RL", "R L")
    s = s.split()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == "R":
            ans[i + 1] += ans[i] // 2 + ans[i] % 2
            ans[i] = ans[i] // 2
        else:
            ans[i - 1] += ans[i] // 2
            ans[i] = ans[i] // 2 + ans[i] % 2
    print(" ".join(map(str, ans)))

=======
Suggestion 8

def solve():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n - 1):
        if s[i] == "R" and s[i + 1] == "L":
            if (i + 1) % 2 == 0:
                ans[i + 1] += 1
            else:
                ans[i] += 1
    for i in range(n):
        if s[i] == "R":
            x = i + 1
            while x < n and s[x] == "R":
                x += 1
            if (i + 1) % 2 == 0:
                ans[x] += (x - i) // 2
                ans[x - 1] += (x - i) // 2 + (x - i) % 2
            else:
                ans[x] += (x - i) // 2 + (x - i) % 2
                ans[x - 1] += (x - i) // 2
            i = x - 1
    for i in range(n - 1, -1, -1):
        if s[i] == "L":
            x = i - 1
            while x >= 0 and s[x] == "L":
                x -= 1
            if (i + 1) % 2 == 0:
                ans[x] += (i - x) // 2
                ans[x + 1] += (i - x) // 2 + (i - x) % 2
            else:
                ans[x] += (i - x) // 2 + (i - x) % 2
                ans[x + 1] += (i - x) // 2
            i = x + 1
    for i in range(n):
        print(ans[i], end=" ")
    print()

=======
Suggestion 9

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    for i in range(n):
        if s[i] == 'L':
            if i%2 == 0:
                ans[i-1] += 1
            else:
                ans[i+1] += 1
        else:
            if i%2 == 0:
                ans[i+1] += 1
            else:
                ans[i-1] += 1
    print(' '.join(map(str,ans)))
