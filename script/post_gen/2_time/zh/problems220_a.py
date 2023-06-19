Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem220a():
    a,b,c=map(int,input().split())
    for i in range(a,b+1):
        if i%c==0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    # A B C = input().split()
    # A, B, C = int(A), int(B), int(C)
    # if A >= 1 and B >= A and B <= 1000 and C >= 1 and C <= 1000:
    #     for i in range(A, B+1):
    #         if i % C == 0:
    #             print(i)
    #             break
    # else:
    #     print(-1)
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 5

def main():
    a,b,c=map(int,input().split())
    result=-1
    for i in range(a,b+1):
        if i%c==0:
            result=i
            break
    print(result)

=======
Suggestion 6

def main():
    #输入
    a,b,c = map(int, input().split())

    #处理
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 7

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)
