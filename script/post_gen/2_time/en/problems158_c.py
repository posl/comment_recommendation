Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    for i in range(1, 1001):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    for i in range(1, 1001):
        if A == int(i * 0.08) and B == int(i * 0.1):
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    ans = -1
    for i in range(1, 1001):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            ans = i
            break
    print(ans)

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    for i in range(1,1001):
        if int(i*0.08) == A and int(i*0.1) == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    for i in range(1, 101):
        if i * 8 // 100 == a and i * 10 // 100 == b:
            print(i)
            return
    print(-1)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if i * 0.08 // 1 == A and i * 0.1 // 1 == B:
            print(i)
            return
    print(-1)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if (i * 8) // 100 == A and (i * 10) // 100 == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if A == i // 0.08 and B == i // 0.1:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 9

def main():
    #write your code here
    a,b=map(int,input().split())
    for i in range(1,1001):
        if int(i*0.08)==a and int(i*0.1)==b:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 10

def main():
    #input
    A, B = map(int, input().split())

    #compute
    for i in range(1, 1001):
        if A == i//1.08 and B == i//1.1:
            print(i)
            break
    else:
        print(-1)

    #output
