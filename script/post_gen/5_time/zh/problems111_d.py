Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    if n == 1:
        print(1)
        print(0)
        print('U')
        return
    if n == 2:
        if x[0] == x[1]:
            print(1)
            print(abs(y[0] - y[1]))
            if y[0] > y[1]:
                print('D')
            else:
                print('U')
        elif y[0] == y[1]:
            print(1)
            print(abs(x[0] - x[1]))
            if x[0] > x[1]:
                print('L')
            else:
                print('R')
        else:
            print(-1)
        return
    if n == 3:
        if x[0] == x[1] and x[0] == x[2]:
            print(1)
            print(abs(y[0] - y[1]) + abs(y[1] - y[2]))
            if y[0] > y[1]:
                print('D')
            else:
                print('U')
            if y[1] > y[2]:
                print('D')
            else:
                print('U')
        elif y[0] == y[1] and y[0] == y[2]:
            print(1)
            print(abs(x[0] - x[1]) + abs(x[1] - x[2]))
            if x[0] > x[1]:
                print('L')
            else:
                print('R')
            if x[1] > x[2]:
                print('L')
            else:
                print('R')
        else:
            print(-1)
        return
    if n == 4:
        if x[0] == x[1] and x[0] == x[2] and x[0] == x[3]:
            print(1)
            print(abs(y[0] - y[1]) + abs(y[1] - y[2]) + abs(y[2] - y[3]))
            if y[0] > y[1]:
                print('D')
            else:

=======
Suggestion 4

def solve():
    return

=======
Suggestion 5

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    if n == 1:
        print(0)
        return
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(0)
            return
        else:
            print(-1)
            return
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j] and y[i] == y[j]:
                print(-1)
                return
    print(2*n)
    for i in range(n):
        if x[i] < 0:
            print(1,-x[i])
        else:
            print(1,x[i])
        print('R'*abs(x[i]),end='')
        if y[i] < 0:
            print('D'*abs(y[i]),end='')
        else:
            print('U'*abs(y[i]),end='')
        print('L',end='')
        if y[i] < 0:
            print('D'*abs(y[i]),end='')
        else:
            print('U'*abs(y[i]),end='')
        print('R',end='')
        if x[i] < 0:
            print('L'*abs(x[i]),end='')
        else:
            print('R'*abs(x[i]),end='')
        print('U',end='')
        if x[i] < 0:
            print('L'*abs(x[i]),end='')
        else:
            print('R'*abs(x[i]),end='')
        print('D',end='')
        if y[i] < 0:
            print('U'*abs(y[i]),end='')
        else:
            print('D'*abs(y[i]),end='')
        print('L',end='')
        if y[i] < 0:
            print('U'*abs(y[i]),end='')
        else:
            print('D'*abs(y[i]),end='')
        print('R',end='')
        if x[i] < 0:
            print('L'*abs(x[i]),end='')
        else:
            print('R'*abs(x[i]),end='')
        print('U',end='')
        if x[i] < 0:
            print('L'*abs
