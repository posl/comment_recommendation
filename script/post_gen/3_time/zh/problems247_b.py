Synthesizing 10/10 solutions

=======
Suggestion 1

def problem247_b():
    print("")

=======
Suggestion 2

def check(n, names):
    for i in range(n):
        for j in range(n):
            if i != j and (names[i][0] == names[j][0] or names[i][0] == names[j][1] or names[i][1] == names[j][0] or names[i][1] == names[j][1]):
                return False
    return True

n = int(input())
names = []
for i in range(n):
    names.append(input().split())

=======
Suggestion 3

def problems247_b():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if names[i][0] == names[j][0] or names[i][0] == names[j][1] or names[i][1] == names[j][0] or names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 4

def get_input():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    return N, names

=======
Suggestion 5

def get_name():
    name_list = []
    while True:
        try:
            name = input()
            if name == "":
                break
            name_list.append(name)
        except EOFError:
            break
    return name_list

=======
Suggestion 6

def get_str():
    n = int(input())
    str_list = []
    for i in range(n):
        str_list.append(input().split())
    return str_list

=======
Suggestion 7

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if name[i][0] == name[j][0] or name[i][1] == name[j][1]:
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
        names.append(input().split())
    for i in range(n):
        for j in range(i+1, n):
            if names[i][0] == names[j][0]:
                print('Yes')
                return
    print('No')

=======
Suggestion 9

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input().split())

    for i in range(N):
        for j in range(N):
            if i != j and name_list[i][0] == name_list[j][0]:
                print("Yes")
                return
            if i != j and name_list[i][1] == name_list[j][1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def check_name(name1, name2):
    if name1 == name2:
        return False
    else:
        return True
