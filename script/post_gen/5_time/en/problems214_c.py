Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    ans[0] = t[0]
    for i in range(1, n):
        ans[i] = min(t[i], ans[i-1] + s[i-1])
    for i in range(n):
        print(ans[i])
    return

=======
Suggestion 2

def main():
    n = int(input())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    ans = [0]*n
    ans[0] = t[0]
    for i in range(1,n):
        ans[i] = min(ans[i-1]+s[i-1],t[i])
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]
    for i in range(N):
        if i == N - 1:
            if ans[i] + S[i] < ans[0]:
                ans[0] = ans[i] + S[i]
        else:
            if ans[i] + S[i] < ans[i + 1]:
                ans[i + 1] = ans[i] + S[i]
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = [0] * N
    for i in range(N):
        ans[i] = T[i]

    for i in range(N):
        if i == N-1:
            if ans[0] > ans[i] + S[i]:
                ans[0] = ans[i] + S[i]
        else:
            if ans[i+1] > ans[i] + S[i]:
                ans[i+1] = ans[i] + S[i]

    for i in range(N):
        print(ans[i])

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    ans = []
    for i in range(n):
        ans.append(t[i])

    for i in range(n):
        if i == 0:
            continue
        if ans[i] > ans[i-1] + s[i-1]:
            ans[i] = ans[i-1] + s[i-1]

    for i in range(n):
        print(ans[i])

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = t[i]
    for i in range(1, n):
        result[i] = min(result[i-1]+s[i-1], result[i])
    for i in range(n):
        print(result[i])

=======
Suggestion 7

def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [10**9+1]*n
    for i in range(n):
        ans[i] = min(ans[i], t[i])
        ans[(i+1)%n] = min(ans[(i+1)%n], ans[i]+s[i])
    for i in ans:
        print(i)

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    #print(N)
    #print(S)
    #print(T)

    #S_1 S_2 ... S_N
    #T_1 T_2 ... T_N

    for i in range(N):
        if i == 0:
            continue
        if T[i] <= T[i-1]:
            T[i] = T[i-1] + S[i-1]

    print(*T, sep='\n')

=======
Suggestion 9

def problem214_c():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T = [0] + T + [0]
    for i in range(1, N+1):
        T[i] = max(T[i], T[i-1]+S[i-1])
    for i in range(1, N+1):
        print(T[i])

=======
Suggestion 10

def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    #print(n, s_list, t_list)
    s_list2 = s_list.copy()
    t_list2 = t_list.copy()
    for i in range(n):
        s_list2[i] = [s_list[i], i]
        t_list2[i] = [t_list[i], i]
    #print(s_list2, t_list2)
    s_list2.sort()
    t_list2.sort()
    #print(s_list2, t_list2)
    s_list3 = s_list2.copy()
    t_list3 = t_list2.copy()
    for i in range(n):
        if i == 0:
            s_list3[i][0] = 0
        else:
            s_list3[i][0] = s_list2[i][0] - s_list2[i-1][0]
        if i == 0:
            t_list3[i][0] = 0
        else:
            t_list3[i][0] = t_list2[i][0] - t_list2[i-1][0]
    #print(s_list3, t_list3)
    s_list3.sort(key=lambda x: x[1])
    t_list3.sort(key=lambda x: x[1])
    #print(s_list3, t_list3)
    ans_list = [0]*n
    for i in range(n):
        ans_list[t_list3[i][1]] = ans_list[s_list3[i][1]] + s_list3[i][0]
    #print(ans_list)
    for i in range(n):
        print(ans_list[i])
