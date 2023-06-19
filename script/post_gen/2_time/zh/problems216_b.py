Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name_list[i][0] == name_list[j][0] and name_list[i][1] == name_list[j][1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    a = [input().split() for i in range(n)]
    print("Yes" if len(set(tuple(i) for i in a)) < n else "No")

=======
Suggestion 3

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    names.sort()
    for i in range(n-1):
        if names[i] == names[i+1]:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    name.sort()
    for i in range(n-1):
        if name[i] == name[i+1]:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())

    for i in range(n):
        for j in range(i+1, n):
            if name_list[i] == name_list[j]:
                print('Yes')
                return
    print('No')

=======
Suggestion 6

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    for i in range(n):
        for j in range(i+1, n):
            if name[i] == name[j]:
                print('Yes')
                exit(0)
    print('No')

=======
Suggestion 7

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
Suggestion 8

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    names.sort()
    for i in range(n-1):
        if names[i] == names[i+1]:
            print("Yes")
            break
        elif i == n-2:
            print("No")

=======
Suggestion 9

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
Suggestion 10

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    names.sort()
    for i in range(N-1):
        if names[i] == names[i+1]:
            print("Yes")
            exit()
    print("No")
