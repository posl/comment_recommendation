Synthesizing 10/10 solutions

=======
Suggestion 1

def f(a, b):
    return a ^ b

=======
Suggestion 2

def cal_xor(a,b):
    if a==b:
        return a
    else:
        return cal_xor(a,b-1)^b

=======
Suggestion 3

def f(a,b):
    if a==b:
        return a
    else:
        return a^f(a+1,b)

=======
Suggestion 4

def f(a, b):
    if a == b:
        return a
    else:
        return f(a, b - 1) ^ b

=======
Suggestion 5

def f(a, b):
    if a == b:
        return a
    return f(a, b - 1) ^ b

=======
Suggestion 6

def f(a, b):
    if a == b:
        return a
    else:
        return f(a, b-1) ^ b

a, b = map(int, input().split())
print(f(a, b))

=======
Suggestion 7

def func(a, b):
    if a == b:
        return a
    else:
        return func(a, b-1) | b

=======
Suggestion 8

def f(a, b):
    #a = int(input("请输入a:"))
    #b = int(input("请输入b:"))
    #a = 123456789012
    #b = 123456789012
    print("a = %d, b = %d"%(a, b))
    result = 0
    for i in range(a, b+1):
        result = result ^ i
    print(result)

f(2, 4)
f(123, 456)
f(123456789012, 123456789012)

=======
Suggestion 9

def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(1, b)
    if a % 2 == 0 and b % 2 == 0:
        return f(a // 2, b // 2) * 2
    if a % 2 == 0 and b % 2 == 1:
        return f(a // 2, b // 2) * 2 + 1
    if a % 2 == 1 and b % 2 == 0:
        return f((a + 1) // 2, b // 2) * 2 - 1
    if a % 2 == 1 and b % 2 == 1:
        return f(a // 2, b // 2) * 2

=======
Suggestion 10

def f(a, b):
    if a == b:
        return a
    if a == 0:
        return f(1, b)
    if a % 2 == 0:
        return f(a - 1, b) ^ a
    else:
        return (f(a - 1, b) ^ a) ^ f(0, a - 1)

a = int(input("请输入a的值:"))
b = int(input("请输入b的值:"))
print("f(", a, ",", b, ")=", f(a, b))
