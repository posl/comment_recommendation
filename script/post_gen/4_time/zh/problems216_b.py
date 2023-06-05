Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())

    for i in range(n):
        for j in range(i+1, n):
            if names[i] == names[j]:
                print('Yes')
                return
    print('No')

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 3

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    if len(name) == len(set(name)):
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    name_list.sort()
    for i in range(N-1):
        if name_list[i] == name_list[i+1]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if data[i][0] == data[j][0] and data[i][1] == data[j][1]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 6

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    print(names)
    for i in range(n):
        for j in range(i+1,n):
            if names[i][0]==names[j][0] and names[i][1]==names[j][1]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 7

def main():
    # 读入数据
    n = int(input())
    # print(n)
    # print(type(n))
    # print(type(input()))
    # print(type(input().split()))
    # print(type(input().split()[0]))
    # print(type(input().split()[1]))
    # print(type(input().split()[0][0]))
    # print(type(input().split()[0][1]))
    # print(type(input().split()[0][2]))
    # print(type(input().split()[0][3]))
    # print(type(input().split()[0][4]))
    # print(type(input().split()[0][5]))
    # print(type(input().split()[0][6]))
    # print(type(input().split()[0][7]))
    # print(type(input().split()[0][8]))
    # print(type(input().split()[0][9]))
    # print(type(input().split()[1][0]))
    # print(type(input().split()[1][1]))
    # print(type(input().split()[1][2]))
    # print(type(input().split()[1][3]))
    # print(type(input().split()[1][4]))
    # print(type(input().split()[1][5]))
    # print(type(input().split()[1][6]))
    # print(type(input().split()[1][7]))
    # print(type(input().split()[1][8]))
    # print(type(input().split()[1][9]))
    # print(type(input().split()[2][0]))
    # print(type(input().split()[2][1]))
    # print(type(input().split()[2][2]))
    # print(type(input().split()[2][3]))
    # print(type(input().split()[2][4]))
    # print(type(input().split()[2][5]))
    # print(type(input().split()[2][6]))
    # print(type(input().split()[2][7]))
    # print(type(input().split()[2][8]))
    # print(type(input().split()[2][9]))
    # print(type(input().split()[3][0]))
    # print(type(input().split()[3][1]))
    # print(type(input().split()[3][2]))
    # print(type(input().split()[3][3]))
    # print(type(input().split()[3][4]))
    # print(type(input().split()[3][5]))
    # print(type(input().split()[

=======
Suggestion 8

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
Suggestion 9

def main():
    n = int(input())
    list1 = []
    for i in range(n):
        list1.append(input())
    if len(list1) == len(set(list1)):
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    n = int(input())
    list = []
    for i in range(n):
        s, t = input().split()
        list.append(s + t)
    if len(list) == len(set(list)):
        print("No")
    else:
        print("Yes")

main()
