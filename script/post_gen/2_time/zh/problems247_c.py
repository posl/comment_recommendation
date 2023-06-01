Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check(s,t):
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                return True
    return False

n = int(input())
s = []
t = []
for i in range(n):
    s.append(input().split()[0])
    t.append(input().split()[1])

for i in range(n):
    for j in range(n):
        if i != j:
            if s[i] == s[j] or t[i] == t[j]:
                print('Yes')
                exit()
print('No')

=======
Suggestion 2

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        if i == 0:
            if name[0][0] == name[1][0] or name[0][0] == name[1][1] or name[0][1] == name[1][0] or name[0][1] == name[1][1]:
                print('Yes')
                break
            else:
                print('No')
                break
        elif i == n-1:
            if name[i][0] == name[i-1][0] or name[i][0] == name[i-1][1] or name[i][1] == name[i-1][0] or name[i][1] == name[i-1][1]:
                print('Yes')
                break
            else:
                print('No')
                break
        else:
            if name[i][0] == name[i-1][0] or name[i][0] == name[i-1][1] or name[i][1] == name[i-1][0] or name[i][1] == name[i-1][1]:
                if name[i][0] == name[i+1][0] or name[i][0] == name[i+1][1] or name[i][1] == name[i+1][0] or name[i][1] == name[i+1][1]:
                    print('Yes')
                    break
                else:
                    print('No')
                    break
            else:
                print('No')
                break

=======
Suggestion 3

def problem247_b():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    for i in range(N):
        for j in range(N):
            if name[i][0] == name[j][1] and i != j:
                print("Yes")
                return
    print("No")

=======
Suggestion 4

def solve():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 5

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def main():
    # 读入数据
    N = int(input())
    s = []
    t = []
    for i in range(N):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)

    # 检查是否有重复
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] and t[i] == t[j]:
                print("No")
                return

    # 检查是否有重名
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j] or t[i] == t[j]:
                print("Yes")
                return

    print("No")

=======
Suggestion 7

def solve():
    N = int(input())
    names = []
    for _ in range(N):
        s, t = input().split()
        names.append(s)
        names.append(t)
    if len(set(names)) == 2*N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().split())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][0] == a[j][0] or a[i][1] == a[j][1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def get_nickname(s,t):
    if len(s) < len(t):
        min_len = len(s)
    else:
        min_len = len(t)
    for i in range(min_len):
        if s[i] != t[i]:
            return s[0:i+1]
    return s[0:min_len+1]
