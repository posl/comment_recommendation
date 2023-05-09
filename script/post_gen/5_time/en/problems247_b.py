Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i] == s[j] and t[i] == t[j]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        tmp = input().split()
        s.append(tmp[0])
        t.append(tmp[1])
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j] and t[i] == t[j]:
                print("No")
                return
    print("Yes")
    return

=======
Suggestion 3

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
            if i != j and s[i] == s[j]:
                print("No")
                return
            if i != j and t[i] == t[j]:
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
        s1, t1 = input().split()
        s.append(s1)
        t.append(t1)

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
            if i != j:
                if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                    print("No")
                    return
    print("Yes")

=======
Suggestion 6

def get_input():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    return n, s, t

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input().split())
    for i in range(n):
        for j in range(n):
            if s[i][0] == s[j][0] and i != j:
                print("Yes")
                return
            if s[i][1] == s[j][1] and i != j:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 8

def main():
    N = int(input())
    name_list = []
    for _ in range(N):
        name_list.append(input().split())
    for i in range(N):
        for j in range(N):
            if i != j:
                if name_list[i][0] == name_list[j][0] or name_list[i][1] == name_list[j][1]:
                    print("Yes")
                    return
    print("No")
    return

=======
Suggestion 9

def main():
    n = int(input())
    name = [input().split() for _ in range(n)]
    name = [i[0] + i[1] for i in name]
    if len(name) == len(set(name)):
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def check_nickname(name, people):
    if name in people:
        return False
    else:
        return True

n = int(input())
people = []
for i in range(n):
    s, t = input().split()
    people.append(s)
    people.append(t)

for i in range(len(people)):
    if check_nickname(people[i], people[:i] + people[i+1:]):
        print("Yes")
        break
else:
    print("No")
