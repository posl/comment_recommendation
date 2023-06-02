Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(a**b)

=======
Suggestion 2

def power(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

=======
Suggestion 3

def main():
    a,b = input().split()
    print(int(a)**int(b))

=======
Suggestion 4

def main():
    print("请输入两个整数，用空格隔开：")
    a,b = map(int,input().split())
    print(a**b)

=======
Suggestion 5

def power(a, b):
    return a**b
