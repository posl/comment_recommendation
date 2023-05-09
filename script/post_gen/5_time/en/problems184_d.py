Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    a, b, c = map(int, input().split())
    print((a * (a + b + c - 1) + b * (b + c - 1) + c * (c - 1)) / (a + b + c - 1))

=======
Suggestion 2

def expected_value(a, b, c):
    return a / (a + b + c) + b / (a + b + c) * (1 + expected_value(a + 1, b - 1, c)) + c / (a + b + c) * (1 + expected_value(a, b + 1, c - 1))

a, b, c = map(int, input().split())
print(expected_value(a, b, c))

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    print((a*b*c)/((a+b)*(b+c)*(c+a)-a*b*c))

=======
Suggestion 4

def main():
    A,B,C = map(int,input().split())
    print(100*(A/(A+B+C)+B/(A+B+C)+C/(A+B+C)-1))

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a == b == c:
        print(1)
    else:
        print((a / (a + b + c)) * (100 / (a + b + c - 99)) + (b / (a + b + c)) * (100 / (a + b + c - 99)) + (c / (a + b + c)) * (100 / (a + b + c - 99)))

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    # print(a,b,c)
    # a=99
    # b=99
    # c=99
    # a=98
    # b=99
    # c=99
    # a=0
    # b=0
    # c=1
    # a=31
    # b=41
    # c=59
    # a=0
    # b=0
    # c=99
    # a=99
    # b=99
    # c=0
    # a=99
    # b=0
    # c=0
    # a=0
    # b=99
    # c=0
    # a=99
    # b=0
    # c=99
    # a=0
    # b=99
    # c=99
    # a=99
    # b=99
    # c=99
    # a=98
    # b=99
    # c=99
    # a=99
    # b=98
    # c=99
    # a=99
    # b=99
    # c=98
    # a=98
    # b=98
    # c=98
    # a=0
    # b=0
    # c=0
    # a=1
    # b=1
    # c=1
    # a=1
    # b=0
    # c=0
    # a=0
    # b=1
    # c=0
    # a=0
    # b=0
    # c=1
    # a=1
    # b=1
    # c=0
    # a=1
    # b=0
    # c=1
    # a=0
    # b=1
    # c=1
    # a=1
    # b=1
    # c=1
    # a=2
    # b=2
    # c=2
    # a=2
    # b=1
    # c=1
    # a=1
    # b=2

=======
Suggestion 7

def main():
    a,b,c = map(int, input().split())
    print((a*b*c)/(a*b+b*c+c*a))

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    print((a*b*c-1)*1.0/(a*b+b*c+c*a))

=======
Suggestion 9

def main():
    a, b, c = map(int, input().split())
    print((a*100+b*100+c*100-300)/(a+b+c))

main()
# %%
