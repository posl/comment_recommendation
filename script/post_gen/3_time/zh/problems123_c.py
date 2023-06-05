Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if N <= min(A,B,C,D,E):
        print(5)
    else:
        print(4 + (N + min(A,B,C,D,E) - 1) // min(A,B,C,D,E))

=======
Suggestion 2

def solve(N,A,B,C,D,E):
    #print(N,A,B,C,D,E)
    if N == 0:
        return 0
    else:
        return min(solve(N//A,A,B,C,D,E)+1, solve(N//B,A,B,C,D,E)+1, solve(N//C,A,B,C,D,E)+1, solve(N//D,A,B,C,D,E)+1, solve(N//E,A,B,C,D,E)+1)

=======
Suggestion 3

def solve():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((N + min(A, B, C, D, E) - 1) // min(A, B, C, D, E) + 4)

=======
Suggestion 4

def problem123_c():
    pass

=======
Suggestion 5

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    min_num = min(a,b,c,d,e)
    time = n // min_num
    if n % min_num != 0:
        time += 1

    print(time+4)

=======
Suggestion 6

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    min_ = min(a, b, c, d, e)
    if n % min_ == 0:
        print(n // min_ + 4)
    else:
        print(n // min_ + 1 + 4)

=======
Suggestion 7

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(4 + (N-1)//min(A,B,C,D,E))

=======
Suggestion 8

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(4 + (n+a-1)//a + (n+b-1)//b + (n+c-1)//c + (n+d-1)//d + (n+e-1)//e)

=======
Suggestion 9

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(int((N + min([A, B, C, D, E]) - 1) / min([A, B, C, D, E])) + 4)

=======
Suggestion 10

def minTime(n, a, b, c, d, e):
    time = 0
    time += (n + a - 1) // a
    time += (n + b - 1) // b
    time += (n + c - 1) // c
    time += (n + d - 1) // d
    time += (n + e - 1) // e
    return time + 4

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(minTime(n, a, b, c, d, e))
