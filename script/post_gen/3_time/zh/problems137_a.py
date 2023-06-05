Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(a+b, a-b, a*b))

=======
Suggestion 2

def max(x, y):
    if x > y:
        return x
    else:
        return y

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    print(max(a+b,a-b,a*b))
main()

=======
Suggestion 4

def main():
    x = input()
    a,b = x.split()
    a = int(a)
    b = int(b)
    c = a + b
    d = a - b
    e = a * b
    print(max(c,d,e))

=======
Suggestion 5

def max_num(a, b):
    if a+b > a-b and a+b > a*b:
        return a+b
    elif a-b > a+b and a-b > a*b:
        return a-b
    else:
        return a*b
