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
        for j in range(i + 1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N-1):
        for j in range(i+1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1, N):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('Yes')
                return
    print('No')

main()

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    if len(set(S)) == len(set(T)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if names[i] == names[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(n):
        for j in range(i+1,n):
            s1, t1 = input().split()
            s2, t2 = input().split()
            if s1 == s2 and t1 == t2:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    names = []
    for i in range(N):
        name = input().split()
        names.append(name)
    for i in range(N-1):
        for j in range(i+1,N):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 8

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return

    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    Nlist = []
    for i in range(N):
        Nlist.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if Nlist[i][0] == Nlist[j][0] and Nlist[i][1] == Nlist[j][1]:
                print('Yes')
                return
    print('No')

=======
Suggestion 10

def readinput():
    n = int(input())
    stlist = []
    for _ in range(n):
        stlist.append(list(input().split()))
    return n,stlist
