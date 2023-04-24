Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(N):
        for j in range(N):
            if i != j:
                if s[i] == s[j] or t[i] == t[j]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    if len(set(s)) == len(set(t)) == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    print("No")
                    return
    print("Yes")

main()

=======
Suggestion 4

def main():
    n = int(input())
    names = []
    for i in range(n):
        s, t = input().split()
        names.append(s)
        names.append(t)
    if len(names) == len(set(names)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    names = [tuple(input().split()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')

=======
Suggestion 6

def main():
    #input
    N = int(input())
    S = [None] * N
    T = [None] * N
    for i in range(N):
        S[i], T[i] = input().split()
    
    #compute
    for i in range(N):
        if S[i] == T[i]:
            print("No")
            return
        for j in range(N):
            if i != j and (S[i] == S[j] or S[i] == T[j] or T[i] == S[j] or T[i] == T[j]):
                print("No")
                return
    print("Yes")
    
    return

=======
Suggestion 7

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    dict = {}
    for i in range(N):
        dict[s[i]] = i
        dict[t[i]] = i
    if len(dict) == 2*N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    nicknames = []
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    nicknames.append(names[i][0])
                    nicknames.append(names[i][1])
                    break
    if len(nicknames) == n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input().split())
    name_list.sort()
    for i in range(n-1):
        if name_list[i][0] == name_list[i+1][0] and name_list[i][1] == name_list[i+1][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 10

def main():
    N = int(input())
    S = [input().split() for _ in range(N)]
    if len(set([s for s, _ in S])) < N and len(set([t for _, t in S])) < N:
        print("No")
    else:
        print("Yes")
