Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, A * B * C, A + B * C, A * B + C, A * (B + C), (A + B) * C))

=======

def main():
    A, B, C = map(int, input().split())
    print(max(A + B + C, A * B * C, A * (B + C), A + B * C, (A + B) * C, A * B + C))

main()

=======

def main():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

=======

def main():
    a,b,c = map(int, input().split())
    print(max(a+b+c, a+b*c, (a+b)*c, a*b+c, a*b*c, a*(b+c)))

=======

def main():
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    x = a + b + c
    y = a * 10 + b + c
    z = a + b * 10 + c
    w = a * 100 + b * 10 + c
    print(max(x, y, z, w))

=======

def main():
    a,b,c = map(int,input().split())
    print(max(a+b+c,a*b*c,(a+b)*c,a*(b+c)))

=======

def solve():
    A, B, C = map(int, input().split())
    print(max(A+B+C, A+B*C, A*B+C, A*B*C))

solve()
