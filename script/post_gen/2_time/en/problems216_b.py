Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    names = [input().split() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N-1):
        for j in range(i+1,N):
            if S[i] == S[j] and T[i] == T[j]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 3

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 4

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 5

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 6

def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if name[i][0] == name[j][0] and name[i][1] == name[j][1]:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def main():
    N = int(input())
    name_list = []
    for i in range(N):
        name_list.append(input().split())
    for i in range(N):
        for j in range(N):
            if i != j:
                if name_list[i][0] == name_list[j][0] and name_list[i][1] == name_list[j][1]:
                    print('Yes')
                    return
    print('No')
    return

=======
Suggestion 8

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    if len(names) != len(set([tuple(i) for i in names])):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    print('Yes' if len(set(map(tuple, name))) != N else 'No')

=======
Suggestion 10

def   main (): 
     n  =   int ( input ()) 
     names  =  [ input (). split ()   for   _   in   range ( n )] 
     names . sort () 
     for   i   in   range ( n - 1 ): 
         if   names [ i ][ 0 ] ==  names [ i + 1 ][ 0 ] and  names [ i ][ 1 ] ==  names [ i + 1 ][ 1 ]: 
             print ( 'Yes' ) 
             return 
     print ( 'No' )
