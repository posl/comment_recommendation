Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    print('Yes' if len(set(name)) != len(name) else 'No')

=======
Suggestion 2

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    for i in range(n-1):
        for j in range(i+1,n):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 3

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    if len(set(name_list)) < N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    name_list = []
    for i in range(n):
        name_list.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name_list[i][0] == name_list[j][0] and name_list[i][1] == name_list[j][1]:
                print('Yes')
                return
    print('No')

=======
Suggestion 5

def main():
    #N = int(input())
    #name_list = []
    #for i in range(N):
    #    name_list.append(input().split())
    #name_list = [['tanaka', 'taro'], ['sato', 'hanako'], ['tanaka', 'taro']]
    name_list = [['sypdgidop', 'bkseq'], ['bajsqz', 'hh'], ['ozjekw', 'mcybmtt'], ['qfeysvw', 'dbo']]
    for i in range(len(name_list)):
        if name_list[i] in name_list[i+1:]:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 6

def main():
    name_list = []
    flag = False
    for i in range(int(input())):
        name = input()
        if name in name_list:
            flag = True
            break
        name_list.append(name)
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    print('Yes' if len(set(names)) < n else 'No')

=======
Suggestion 8

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input())
    if len(name_list) == len(set(name_list)):
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    for i in range(n):
        for j in range(i+1,n):
            if name[i] == name[j]:
                print('Yes')
                return
    print('No')
main()

=======
Suggestion 10

def main():
    n = int(input())
    data = []
    for i in range(n):
        data.append(input())
    data.sort()
    for i in range(n-1):
        if data[i] == data[i+1]:
            print("Yes")
            break
    else:
        print("No")
