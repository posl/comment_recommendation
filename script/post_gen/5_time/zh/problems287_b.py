Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)
main()

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    T = []
    for i in range(M):
        T.append(input())
    count = 0
    for t in T:
        for s in S:
            if t == s[-3:]:
                count += 1
                break
    print(count)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if S[i][-3:] == T[j]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    # 读取输入
    N,M = map(int,input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # 答案
    ans = 0
    # 遍历N个字符串
    for i in range(N):
        # 遍历M个字符串
        for j in range(M):
            # 如果S[i]的最后三个字符与T[j]的最后三个字符一致
            if S[i][-3:] == T[j]:
                # 答案加1
                ans += 1
                # 跳出循环
                break
    # 输出答案
    print(ans)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    num = 0
    for i in range(M):
        for j in range(N):
            if T[i] in S[j]:
                num += 1
    print(num)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for j in range(m):
        t.append(input())
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:6] == t[j]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if s[i][3:] == t[j]:
                cnt += 1
                break
    print(cnt)
