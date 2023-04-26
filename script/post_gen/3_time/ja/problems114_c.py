Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(357, N+1):
        if "3" in str(i) and "5" in str(i) and "7" in str(i):
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    cnt = 0
    for i in range(357, N+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                num = i * 100 + j * 10 + k
                if num > N:
                    continue
                if i == 7 or j == 7 or k == 7:
                    if i == 5 or j == 5 or k == 5:
                        if i == 3 or j == 3 or k == 3:
                            ans += 1
    print(ans)
main()

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                if i == 7 or i == 5 or i == 3:
                    if j == 7 or j == 5 or j == 3:
                        if k == 7 or k == 5 or k == 3:
                            num = 100 * i + 10 * j + k
                            if num <= N:
                                ans += 1
    print(ans)

=======
Suggestion 5

def check753(num):
    num = str(num)
    if num.count("7") > 0 and num.count("5") > 0 and num.count("3") > 0:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(3,10):
        for j in range(3,10):
            for k in range(3,10):
                if i == 7 or i == 5 or i == 3:
                    if j == 7 or j == 5 or j == 3:
                        if k == 7 or k == 5 or k == 3:
                            num = int(str(i) + str(j) + str(k))
                            if num <= N:
                                ans += 1
    print(ans)

=======
Suggestion 7

def is753(n):
    return '7' in str(n) and '5' in str(n) and '3' in str(n)

=======
Suggestion 8

def solve():
    #import sys
    #input = sys.stdin.readline
    N = int(input())
    ans = 0
    def dfs(s):
        nonlocal ans
        if int(s) > N:
            return
        if all(s.count(c) > 0 for c in '753'):
            ans += 1
        for c in '753':
            dfs(s + c)
    dfs('0')
    print(ans)

=======
Suggestion 9

def is753(n):
    if n < 100:
        return False
    if n < 1000:
        return n % 10 in [3, 5, 7] and n % 100 // 10 in [3, 5, 7] and n // 100 in [3, 5, 7]
    return is753(n % 10) and is753(n // 10)

n = int(input())
ans = 0
for i in range(357, n + 1):
    if is753(i):
        ans += 1
print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    print(solve(N))
