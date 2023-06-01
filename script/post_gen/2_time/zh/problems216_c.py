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
            if name_list[i] == name_list[j]:
                print("Yes")
                return
    print("No")
main()

=======
Suggestion 2

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    name_list.sort()
    for i in range(n-1):
        if name_list[i] == name_list[i+1]:
            print('Yes')
            return
    print('No')
main()

=======
Suggestion 3

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    name_list.sort()
    for i in range(n-1):
        if name_list[i] == name_list[i+1]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    if len(name_list) == len(set(name_list)):
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def get_input():
    input_data = []
    while True:
        try:
            line = input()
            if line == '':
                break
            input_data.append(line)
        except EOFError:
            break
    return input_data

=======
Suggestion 6

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if names[i][0]==names[j][0] and names[i][1]==names[j][1]:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 7

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    if len(set(name_list)) == len(name_list):
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input().split())
    name_list.sort()
    for i in range(n-1):
        if name_list[i] == name_list[i+1]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 9

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input())
    for i in range(n):
        for j in range(i + 1, n):
            if name_list[i] == name_list[j]:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input())
    if len(names) == len(set(names)):
        print("No")
    else:
        print("Yes")
