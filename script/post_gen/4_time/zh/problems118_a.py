Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b=map(int,input().split())
    if b%a==0:
        print(a+b)
    else:
        print(b-a)

=======
Suggestion 2

def div(a,b):
    if b%a == 0:
        print(a+b)
    else:
        print(b-a)

=======
Suggestion 3

def main():
    # 读取输入
    # 读取输入
    line = input()
    line = line.split()
    #print(line)
    a = int(line[0])
    b = int(line[1])
    #print(a,b)
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

=======
Suggestion 5

def main():
    # 读取输入
    a, b = map(int, input().split())
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)
