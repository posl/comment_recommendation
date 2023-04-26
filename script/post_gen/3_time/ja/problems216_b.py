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
            if i == j:
                continue
            if S[i] == S[j] and T[i] == T[j]:
                print('Yes')
                return
    print('No')
main()

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

    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print('Yes')
                return
    print('No')

=======
Suggestion 3

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        a, b = input().split()
        s.append(a)
        t.append(b)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j] and t[i] == t[j]:
                print("Yes")
                exit()
    print("No")

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
    if len(S) != len(set(S)) or len(T) != len(set(T)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if names[i] == names[j]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 6

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    name.sort()
    for i in range(n-1):
        if name[i][0] == name[i+1][0] and name[i][1] == name[i+1][1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input())

    if len(names) != len(set(names)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    st = []
    for _ in range(n):
        s, t = input().split()
        st.append(s + t)
    if len(set(st)) == n:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    N = int(input())
    list = []
    for i in range(N):
        S, T = input().split()
        list.append(S + T)
    if len(set(list)) == len(list):
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    print('No')
