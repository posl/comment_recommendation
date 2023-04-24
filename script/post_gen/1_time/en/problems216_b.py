Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    names = set()
    for i in range(N):
        name = input()
        if name in names:
            print("Yes")
            return
        else:
            names.add(name)
    print("No")
    return

=======
Suggestion 2

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
Suggestion 3

def solve():
    n = int(input())
    names = set()
    for i in range(n):
        name = input()
        if name in names:
            print("Yes")
            return
        names.add(name)
    print("No")

solve()

=======
Suggestion 4

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())

    names.sort()

    for i in range(n-1):
        if names[i] == names[i+1]:
            print("Yes")
            return

    print("No")

main()

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    if len(s) != len(set(s)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if name_list[i] == name_list[j]:
                print('Yes')
                return
    print('No')

=======
Suggestion 7

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        if name not in names:
            names.append(name)
        else:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 8

def main():
    names = []
    for i in range(int(input())):
        names.append(input())
    if len(set(names)) == len(names):
        print("No")
    else:
        print("Yes")

=======
Suggestion 9

def main():
    N = int(input())
    ST = [input().split() for _ in range(N)]
    ST.sort()
    for i in range(N-1):
        if ST[i][0] == ST[i+1][0] and ST[i][1] == ST[i+1][1]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 10

def get_input():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    return names
