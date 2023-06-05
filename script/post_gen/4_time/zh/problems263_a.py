Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a,b,c,d,e = map(int,input().split())
    if a == b == c or a == b == d or a == b == e or a == c == d or a == c == e or a == d == e or b == c == d or b == c == e or b == d == e or c == d == e:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = input()
    nlist = n.split()
    nset = set(nlist)
    if len(nset) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    num_list = list(map(int, input().split()))
    num_list.sort()
    if num_list[0]==num_list[1] and num_list[1]==num_list[2] and num_list[3]==num_list[4]:
        print('Yes')
    elif num_list[0]==num_list[1] and num_list[2]==num_list[3] and num_list[3]==num_list[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a,b,c,d,e = map(int, input().split())
    if (a==b==c) or (a==b==d) or (a==b==e) or (a==c==d) or (a==c==e) or (a==d==e) or (b==c==d) or (b==c==e) or (b==d==e) or (c==d==e):
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a = input().split()
    if a.count(a[0]) == 3 and a.count(a[1]) == 2:
        print('Yes')
    elif a.count(a[0]) == 2 and a.count(a[1]) == 3:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    if a[0] == a[1] and a[1] != a[2] and a[2] == a[3] and a[3] == a[4]:
        print("Yes")
    elif a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    a.sort()
    if (a[0] == a[1] and a[1] == a[2] and a[3] == a[4]) or (a[0] == a[1] and a[2] == a[3] and a[3] == a[4]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a,b,c,d,e = map(int,input().split())
    if (a==b and b==c) or (a==b and b==d) or (a==b and b==e) or (a==c and c==d) or (a==c and c==e) or (a==d and d==e) or (b==c and c==d) or (b==c and c==e) or (b==d and d==e) or (c==d and d==e):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    a = input()
    a = a.split()
    if a[0] == a[1] and a[1] == a[2]:
        if a[3] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[1] and a[1] == a[3]:
        if a[2] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[1] and a[1] == a[4]:
        if a[2] == a[3]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[2] and a[2] == a[3]:
        if a[1] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[2] and a[2] == a[4]:
        if a[1] == a[3]:
            print("Yes")
        else:
            print("No")
    elif a[0] == a[3] and a[3] == a[4]:
        if a[1] == a[2]:
            print("Yes")
        else:
            print("No")
    elif a[1] == a[2] and a[2] == a[3]:
        if a[0] == a[4]:
            print("Yes")
        else:
            print("No")
    elif a[1] == a[2] and a[2] == a[4]:
        if a[0] == a[3]:
            print("Yes")
        else:
            print("No")
    elif a[1] == a[3] and a[3] == a[4]:
        if a[0] == a[2]:
            print("Yes")
        else:
            print("No")
    elif a[2] == a[3] and a[3] == a[4]:
        if a[0] == a[1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()
