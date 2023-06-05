Synthesizing 10/10 solutions

=======
Suggestion 1

def S(n):
    if n == 1:
        return [1]
    else:
        s = S(n-1)
        return s + [n] + s

n = int(input())
print(*S(n))

=======
Suggestion 2

def printS(n):
    if n == 1:
        print(1,end=' ')
    else:
        printS(n-1)
        print(n,end=' ')
        printS(n-1)

n = int(input())
printS(n)
print()

=======
Suggestion 3

def f(n):
    if n == 1:
        return [1]
    else:
        tmp = f(n-1)
        return tmp + [n] + tmp

n = int(input())
print(' '.join(map(str, f(n))))

=======
Suggestion 4

def printS(n):
    if n == 1:
        return "1"
    else:
        return printS(n-1) + " " + str(n) + " " + printS(n-1)
n = int(input())
print(printS(n))

=======
Suggestion 5

def f(n):
    if n==1:
        return [1]
    else:
        return f(n-1)+[n]+f(n-1)

n=int(input())
print(' '.join(map(str,f(n))))

=======
Suggestion 6

def main():
    n = int(input())
    print("1",end="")
    for i in range(2,n+1):
        print(" "+str(i),end="")
        print(" 1",end="")
    print()

main()

=======
Suggestion 7

def sequence(n):
    if n == 1:
        return [1]
    else:
        seq = sequence(n-1)
        return seq + [n] + seq

=======
Suggestion 8

def func(n):
    if n == 1:
        return [1]
    else:
        return func(n-1) + [n] + func(n-1)

n = int(input())
print(*func(n))

=======
Suggestion 9

def sequence(n):
    if n == 1:
        return [1]
    else:
        s = sequence(n-1)
        return s + [n] + s

=======
Suggestion 10

def s(n):
    if n == 1:
        return [1]
    else:
        return s(n-1) + [n] + s(n-1)

n = int(input())
print(*s(n))
