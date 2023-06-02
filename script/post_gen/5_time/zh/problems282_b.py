Synthesizing 10/10 solutions

=======
Suggestion 1

def check(s1, s2, M):
    for i in range(M):
        if s1[i] == 'x' and s2[i] == 'x':
            return False
    return True

=======
Suggestion 2

def solve():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            cnt = 0
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

solve()

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            cnt = 0
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    cnt += 1
            if cnt == m:
                ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    l = []
    for i in range(n):
        l.append(input())
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(m):
                if l[i][k] == 'o' or l[j][k] == 'o':
                    if k == m-1:
                        cnt += 1
                else:
                    break
    print(cnt)

=======
Suggestion 5

def main():
    # 读取输入
    input_line = input()
    input_line_list = input_line.split(" ")
    N = int(input_line_list[0])
    M = int(input_line_list[1])
    input_str_list = []
    for i in range(N):
        input_str_list.append(input())
    # print(N,M,input_str_list)

    # 处理
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            # print(i,j)
            flag = True
            for k in range(M):
                if input_str_list[i][k] == "x" and input_str_list[j][k] == "x":
                    flag = False
                    break
            if flag:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            cnt = 0
            for k in range(M):
                if S[i][k] == 'o' or S[j][k] == 'o':
                    cnt += 1
            if cnt == M:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    # 读取输入
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    # 答案
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if all(S[i][k] == 'o' or S[j][k] == 'o' for k in range(M)):
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ok = True
            for k in range(m):
                if s[i][k] == 'x' and s[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ok = True
            for k in range(M):
                if S[i][k] == 'x' and S[j][k] == 'x':
                    ok = False
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    n,m=map(int,input().split())
    s=[]
    for i in range(n):
        s.append(input())
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            ok=True
            for k in range(m):
                if s[i][k]!='o' and s[j][k]!='o':
                    ok=False
            if ok:
                ans+=1
    print(ans)
solve()
