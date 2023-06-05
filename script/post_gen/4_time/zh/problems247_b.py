Synthesizing 10/10 solutions

=======
Suggestion 1

def check_name(name, names):
    for n in names:
        if name == n:
            return False
    return True

=======
Suggestion 2

def readinput():
    n=int(input())
    st=[]
    for _ in range(n):
        s,t=input().split()
        st.append((s,t))
    return n,st

=======
Suggestion 3

def check(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return False
    return True

n = int(input())
a = []
for i in range(n):
    s, t = input().split()
    a.append(s)
    a.append(t)

=======
Suggestion 4

def problem247_b():
    n = int(input())
    people = []
    for i in range(n):
        people.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if people[i][0] == people[j][0] or people[i][1] == people[j][1]:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 5

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def solve(N, S, T):
    if N == 2:
        if S[0] == S[1] or S[0] == T[1] or T[0] == S[1] or T[0] == T[1]:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(N):
            for j in range(N):
                if i != j:
                    if S[i] == S[j] or S[i] == T[j] or T[i] == S[j] or T[i] == T[j]:
                        print("No")
                        return
        print("Yes")

=======
Suggestion 7

def judge(a, b):
    if a == b:
        return False
    else:
        return True

=======
Suggestion 8

def check(n, namelist):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if namelist[i][0] == namelist[j][0] or namelist[i][0] == namelist[j][1] or namelist[i][1] == namelist[j][0] or namelist[i][1] == namelist[j][1]:
                return False
    return True

=======
Suggestion 9

def check(s,t):
    if s == t:
        return False
    return True

=======
Suggestion 10

def main():
    N=int(input())
    s=[]
    t=[]
    for i in range(N):
        a,b=input().split()
        s.append(a)
        t.append(b)

    #print(s)
    #print(t)
    flag=0
    for i in range(N):
        for j in range(N):
            if i!=j:
                if s[i]==s[j] and t[i]==t[j]:
                    flag=1
                    break
    if flag==1:
        print("No")
    else:
        print("Yes")

main()
