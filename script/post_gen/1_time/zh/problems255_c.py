Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, a, d, n = map(int, input().split())
    cnt = 0
    while x != a:
        if x > a:
            x -= 1
        else:
            x += 1
        cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if n == 1:
            print(abs(x-a))
        else:
            if x < a:
                if d > 0:
                    print(min(abs(x-a),abs(x-a-d*(n-1))))
                else:
                    print(abs(x-a))
            else:
                if d > 0:
                    print(abs(x-a))
                else:
                    print(min(abs(x-a),abs(x-a-d*(n-1))))
main()

=======
Suggestion 3

def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        ans = 0
        if x < a:
            while x != a:
                x += 1
                ans += 1
        else:
            while x != a:
                x -= 1
                ans += 1
        print(ans)

=======
Suggestion 4

def main():
    x, a, d, n = map(int, input().split())
    cnt = 0
    if d == 0:
        if x != a:
            cnt = 2
        else:
            cnt = 0
    elif n == 1:
        if x != a:
            cnt = 2
        else:
            cnt = 0
    else:
        if (x - a) % d == 0:
            cnt = 0
        else:
            cnt = 2
    print(cnt)

=======
Suggestion 5

def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print("inf")
        return
    if N == 1:
        if X == A:
            print(0)
        else:
            print("inf")
        return
    if D > 0:
        if X < A or (X-A) % D != 0:
            print("inf")
            return
    else:
        if X > A or (X-A) % D != 0:
            print("inf")
            return
    if D > 0:
        if (X-A) // D >= 0:
            print((X-A) // D)
        else:
            print("inf")
    else:
        if (X-A) // D <= 0:
            print((X-A) // D)
        else:
            print("inf")

=======
Suggestion 6

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        ans = 0
        while True:
            if x == a:
                print(ans)
                return
            if x < a:
                if (a - x) % d == 0:
                    print(ans + (a - x) // d)
                else:
                    print(ans + (a - x) // d + 1)
                return
            if n == 0:
                print(ans + x - a)
                return
            if x - a > d:
                ans += 1
                x -= 1
            else:
                ans += 1
                x += 1
            n -= 1

=======
Suggestion 7

def main():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if n == 1:
            if x == a:
                print(0)
            else:
                print(1)
        else:
            if x < a:
                if (a - x) % d == 0:
                    print((a - x) // d)
                else:
                    print(1 + (a - x) // d)
            else:
                if (x - a) % d == 0:
                    print((x - a) // d)
                else:
                    print(1 + (x - a) // d)

=======
Suggestion 8

def main():
    x,a,d,n = map(int,input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(-1)
    else:
        if d > 0:
            if x < a:
                print(-1)
            else:
                if (x-a)%d == 0:
                    print((x-a)//d)
                else:
                    print(-1)
        else:
            if x > a:
                print(-1)
            else:
                if (a-x)%(-d) == 0:
                    print((a-x)//(-d))
                else:
                    print(-1)

=======
Suggestion 9

def main():
    x,a,d,n = map(int, input().split())
    if d == 0:
        if x == a:
            print(0)
        else:
            print(1)
    else:
        if (x-a)%d == 0 and (x-a)//d >= 0:
            print((x-a)//d)
        else:
            print(-1)

=======
Suggestion 10

def solve(X,A,D,N):
    if D == 0:
        if X == A:
            return 0
        else:
            return -1
    if N == 1:
        if X == A:
            return 0
        else:
            return -1
    if N == 2:
        if X == A or X == A + D:
            return 0
        else:
            return -1
    if (X - A) % D != 0:
        return -1
    else:
        return (X - A) // D

X,A,D,N = map(int,input().split())
print(solve(X,A,D,N))
