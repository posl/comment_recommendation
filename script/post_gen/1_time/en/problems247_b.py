Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                    print('No')
                    return
    print('Yes')

=======
Suggestion 2

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                print("Yes")
                return
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
            if i == j:
                continue
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("No")
                return
    print("Yes")

=======
Suggestion 4

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input().split()[0])
        t.append(input().split()[1])
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] and t[i] == t[j]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j and (names[i][0] == names[j][0] or names[i][1] == names[j][1]):
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 6

def main():
    n = int(input())
    st = []
    for i in range(n):
        st.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if st[i][0] == st[j][0] and st[i][1] == st[j][1]:
                    print('No')
                    exit()
    print('Yes')

=======
Suggestion 7

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    for i in range(n):
        for j in range(n):
            if i != j and names[i] == names[j]:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 8

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if i != j and (names[i][0] == names[j][0] or names[i][1] == names[j][1]):
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input().split())
    flag = False
    for i in range(N):
        for j in range(N):
            if i != j:
                if name_list[i][0] == name_list[j][0] and name_list[i][1] == name_list[j][1]:
                    flag = True
                if name_list[i][0] == name_list[j][0] or name_list[i][1] == name_list[j][1]:
                    flag = True
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())

    names = [x for x in zip(*names)]
    names = names[0] + names[1]
    if len(names) != len(set(names)):
        print('Yes')
    else:
        print('No')
