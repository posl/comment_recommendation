Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                if i != j:
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
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    #print(s)
    #print(t)
    a = []
    for i in range(n):
        if s[i] in t:
            a.append(s[i])
        else:
            a.append(t[i])
    #print(a)
    if len(a) == len(set(a)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if name[i][0] == name[j][0] and i != j:
                print("No")
                return
            if name[i][1] == name[j][1] and i != j:
                print("No")
                return
    print("Yes")
    return

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
        if s[i] in s[:i] or s[i] in s[i+1:] or s[i] in t[:i] or s[i] in t[i+1:]:
            if t[i] in s[:i] or t[i] in s[i+1:] or t[i] in t[:i] or t[i] in t[i+1:]:
                print('No')
                exit()
    print('Yes')

=======
Suggestion 5

def main():
    n = int(input())
    dict = {}
    for i in range(n):
        s,t = input().split()
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    for key in dict:
        if dict[key] > 1:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 6

def main():
    n = int(input())
    s = [input().split() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and (s[i][0] == s[j][0] or s[i][1] == s[j][1]):
                break
        else:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 7

def main():
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_, t_ = input().split()
        s.append(s_)
        t.append(t_)
    a = []
    for i in range(N):
        if s[i] in a or t[i] in a:
            print('No')
            return
        a.append(s[i])
        a.append(t[i])
    print('Yes')

=======
Suggestion 8

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    flag = True
    for i in range(N):
        for j in range(N):
            if i != j:
                if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
                    flag = False
    if flag:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 9

def main():
    N = int(input())
    s = [input().split() for _ in range(N)]
    for i in range(N):
        if s[i][0] in s[i][1] or s[i][1] in s[i][0]:
            continue
        else:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 10

def main():
    N = int(input())
    #名前のリスト
    name_list = [input().split() for i in range(N)]
    #名前の辞書
    name_dict = {}
    for i in range(N):
        name_dict[name_list[i][0]] = 0
        name_dict[name_list[i][1]] = 0

    for i in range(N):
        if name_dict[name_list[i][0]] == 0 and name_dict[name_list[i][1]] == 0:
            name_dict[name_list[i][0]] = 1
            name_dict[name_list[i][1]] = 1
        else:
            print("No")
            return

    print("Yes")
