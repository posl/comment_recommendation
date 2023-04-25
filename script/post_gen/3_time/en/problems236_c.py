Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    ans = []
    for i in range(N):
        if S[i] in T:
            ans.append('Yes')
        else:
            ans.append('No')
    print('

'.join(ans))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    ans = []
    for i in range(N):
        if S[i] in T:
            ans.append("Yes")
        else:
            ans.append("No")
    print(*ans, sep = "

")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    i = 0
    j = 0
    ans = []
    while i < N:
        if j < M and S[i] == T[j]:
            ans.append('Yes')
            j += 1
        else:
            ans.append('No')
        i += 1
    print('

'.join(ans))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    ans = [0] * N
    for i in range(N):
        if S[i] in T:
            ans[i] = 1
    for i in range(N):
        if ans[i] == 1:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    S_set = set(S)
    T_set = set(T)
    S_T = S_set & T_set
    for i in range(N):
        if S[i] in S_T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    # Express trains may stop at all stations.
    if n == m:
        print('Yes' * n)
        return
    # Express trains may stop at only M (M ≦ N) stations.
    # T_1 = S_1 and T_M = S_N.
    # (T_1, ..., T_M) is obtained by removing zero or more strings from (S_1, ..., S_N) and lining up the remaining strings without changing the order.
    i = 0
    j = 0
    while i < n:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
        if j == m:
            break
    if j == m:
        print('Yes' * (i - m) + 'No' * (n - i + m) + 'Yes' * m)
    else:
        print('No' * n)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #print(N,M)
    #print(S)
    #print(T)
    #print(S[0])
    #print(T[0])
    #print(S[-1])
    #print(T[-1])
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')
