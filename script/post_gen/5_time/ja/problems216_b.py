Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if len(names) == len(set(names)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input().split())
    name_set = set()
    for name in name_list:
        if tuple(name) in name_set:
            print('Yes')
            return
        else:
            name_set.add(tuple(name))
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input())
    if len(set(name)) != len(name):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def check_duplication(names):
    for i in range(0, len(names)-1):
        for j in range(i+1, len(names)):
            if names[i] == names[j]:
                return True
    return False

=======
Suggestion 5

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if len(names) != len(set(names)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                exit()

    print("No")

=======
Suggestion 7

def problems216_b():
    n = int(input())
    names = []
    for i in range(n):
        s,t = input().split()
        names.append((s,t))

    for i in range(n):
        for j in range(i+1,n):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 8

def main():
    n=int(input())
    s=[]
    t=[]
    for i in range(n):
        a,b=input().split()
        s.append(a)
        t.append(b)
    for i in range(n):
        for j in range(i+1,n):
            if s[i]==s[j] and t[i]==t[j]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 9

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    if len(s) == n:
        print('No')
    else:
        print('Yes')

=======
Suggestion 10

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
            if i == j:
                continue
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return
    print("No")
