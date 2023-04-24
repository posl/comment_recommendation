Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    for i in range(1000):
        if i * 8 // 100 == a and i * 10 // 100 == b:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if int(i*0.08) == A and int(i*0.1) == B:
            print(i)
            return
    print(-1)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    for i in range(1000):
        if A == int(i * 0.08) and B == int(i * 0.1):
            print(i)
            return
    print(-1)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    for i in range(1, 1001):
        if i * 0.08 == A and i * 0.1 == B:
            print(i)
            return
    print(-1)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000):
        if (i * 0.08) // 1 == A and (i * 0.1) // 1 == B:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    for i in range(1, 100000):
        if (i * 8 // 100 == A) and (i * 10 // 100 == B):
            print(i)
            exit()
    print(-1)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    ans = -1
    for i in range(1000):
        if A == i*8//100 and B == i*10//100:
            ans = i
            break
    print(ans)

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    for i in range(1, 1000000000):
        if A == int(i * 0.08) and B == int(i * 0.1):
            print(i)
            return
    print(-1)

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    for i in range(1,1001):
        if a == i*0.08 and b == i*0.1:
            print(i)
            return
    print(-1)

=======
Suggestion 10

def main():
    #入力
    A, B = map(int, input().split())
    #出力
    for i in range(1,1000):
        if i*0.08 == int(i*0.08) and i*0.1 == int(i*0.1):
            if int(i*0.08) == A and int(i*0.1) == B:
                print(i)
                exit()
    print(-1)
