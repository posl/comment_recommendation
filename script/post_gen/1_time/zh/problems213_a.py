Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    C = A ^ B
    print(C)

=======
Suggestion 2

def xor(a, b):
    return a ^ b

=======
Suggestion 3

def xor(a,b):
    return int(bin(a^b)[2:])

=======
Suggestion 4

def xor(a,b):
    return a^b
a,b = map(int,input().split())
print(xor(a,b))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(a^b)

=======
Suggestion 6

def xor(A,B):
    return A^B

=======
Suggestion 7

def problem213_a():
    # 输入
    A,B = map(int,input().split())
    # 输出
    print(A^B)
