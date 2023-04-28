Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(N):
            if i != j:
                if S[i] == S[j] and T[i] == T[j]:
                    print('Yes')
                    return
    print('No')
    return

=======
Suggestion 2

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    for i in range(n):
        for j in range(i+1, n):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('Yes')
                return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    if len(name) == len(set(name)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    N = int(input())
    S_T = [input().split() for i in range(N)]
    for i in range(N):
        for j in range(i+1,N):
            if S_T[i][0] == S_T[j][0] and S_T[i][1] == S_T[j][1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    t = []

    for i in range(n):
        temp = input().split()
        s.append(temp[0])
        t.append(temp[1])

    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j]:
                    if t[i] == t[j]:
                        print("Yes")
                        exit()

    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())

    for i in range(N):
        for j in range(i+1,N):
            if names[i] == names[j]:
                print("Yes")
                return

    print("No")

=======
Suggestion 8

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if len(set(names)) < n:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def problem216b():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_tmp, t_tmp = input().split()
        s.append(s_tmp)
        t.append(t_tmp)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    # N = int(input())
    # s = []
    # t = []
    # for i in range(N):
    #     s.append(input().split()[0])
    #     t.append(input().split()[1])
    # # print(s)
    # # print(t)
    # for i in range(N):
    #     for j in range(i+1, N):
    #         if s[i] == s[j] and t[i] == t[j]:
    #             print("Yes")
    #             exit()
    # print("No")

    N = int(input())
    s = set()
    for i in range(N):
        s.add(input())
    if len(s) == N:
        print("No")
    else:
        print("Yes")
