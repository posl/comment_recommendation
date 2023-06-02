Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    if len(name_list) == len(set(name_list)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    print("请输入N的值：")
    N = int(input())
    print("请输入人名：")
    name = []
    for i in range(N):
        name.append(input())
    for i in range(N):
        for j in range(i+1,N):
            if name[i]==name[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 4

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    print('Yes' if len(names) != len(set(names)) else 'No')

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 6

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        if name in names:
            print('Yes')
            break
        else:
            names.append(name)
    else:
        print('No')

=======
Suggestion 7

def questionB():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    if len(set(name)) == len(name):
        print("No")
    else:
        print("Yes")

questionB()

=======
Suggestion 8

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input())
    if len(name) != len(set(name)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    for i in range(N):
        for j in range(i+1,N):
            if name_list[i] == name_list[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    names.sort()
    for i in range(n-1):
        if names[i] == names[i+1]:
            print("Yes")
            break
    else:
        print("No")
