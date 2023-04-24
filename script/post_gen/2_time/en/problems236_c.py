Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for s in S:
        if s in T:
            print('Yes')
        else:
            print('No')

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
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

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
Suggestion 6

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()

    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def problems236_c():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if len(set(s) & set(t)) == 0:
        print("No")
        return
    print("Yes")
    return

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    # print(N, M, S, T)
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    ans = ["No"] * N
    for i in range(M):
        ans[S.index(T[i])] = "Yes"
    print("\n".join(ans))
