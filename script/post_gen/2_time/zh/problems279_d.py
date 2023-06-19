Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    #print(a,b)
    #print(type(a),type(b))
    #print(a/b)
    #print(a//b)
    #print(a%b)
    #print(a**0.5)

=======
Suggestion 2

def solve():
    A,B = map(int,input().split())
    #A,B = 10,1
    #A,B = 5,10
    #A,B = 1000000000000000000,100
    #print(A,B)
    #print(A**0.5)
    #print(A**(1/2))
    #print(A**0.5)

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    print(b*((a)**(1/2)))

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    print((a + b) / 2)

=======
Suggestion 6

def f(x):
    return A * x + (B / (x ** 0.5))

A, B = map(int, input().split())
l, r = 0, 10 ** 9
for _ in range(100):
    c1 = (2 * l + r) / 3
    c2 = (l + 2 * r) / 3
    if f(c1) < f(c2):
        r = c2
    else:
        l = c1
print(f(l))

=======
Suggestion 7

def solve():
    pass

=======
Suggestion 8

def solve(A: int, B: int):
    pass

=======
Suggestion 9

def solve():
    a,b = map(int,input().split())
    ans = 1e18
    for i in range(1,100000):
        t = 1 + (a + b * i) ** 0.5
        t = t / i
        ans = min(ans,t)
    print(ans)

solve()
