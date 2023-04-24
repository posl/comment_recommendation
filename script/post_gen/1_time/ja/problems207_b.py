Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
        return
    if C * D <= B:
        print(0)
        return
    if A <= B * C:
        print(1)
        return
    print((A - B * C + (C * D - B) - 1) // (C * D - B) + 1)

=======
Suggestion 2

def solve():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print(-1)
        return
    ans = 0
    while A > C * D:
        A -= B
        ans += 1
    print(ans)
    return

=======
Suggestion 3

def solve():
    A, B, C, D = map(int, input().split())
    if B >= C*D:
        print(-1)
    else:
        count = 0
        while A > 0:
            count += 1
            A -= B
            if A <= 0:
                break
            A += C
        print(count)

=======
Suggestion 4

def main():
    a, b, c, d = map(int, input().split())
    if a <= b * d:
        print(-1)
        return
    ans = 0
    while a > c * d:
        a += b
        c += d
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    a,b,c,d = map(int, input().split())
    if a <= b:
        print(-1)
        return
    if d*c <= b:
        print(-1)
        return
    ans = 0
    while a > b:
        a += c
        b += d
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    a, b, c, d = map(int, input().split())
    if a < b:
        print(-1)
        return
    if d * c <= b:
        print(0)
        return
    if a <= c * d - b:
        print(-1)
        return

    ans = (a - b + c - d - 1) // (c - d)
    print(ans)

=======
Suggestion 7

def solve():
    A, B, C, D = map(int, input().split())

    if A <= B * D:
        print(-1)
        return

    ans = 0
    while True:
        if A <= C * ans:
            print(ans)
            return
        A += B
        ans += 1

=======
Suggestion 8

def main():
    a,b,c,d = map(int,input().split())
    if a <= b * d:
        print(-1)
        return
    else:
        if a % (b * d - c) == 0:
            print(int(a / (b * d - c)))
        else:
            print(int(a / (b * d - c) + 1))

=======
Suggestion 9

def main():
    A,B,C,D = map(int,input().split())
    if A <= B * D:
        print(-1)
    else:
        count = 0
        while True:
            if (A - C * count) <= B * count:
                print(count)
                break
            count += 1

=======
Suggestion 10

def get_input_lines_int_array():
    return list(map(int, input().split()))

A, B, C, D = get_input_lines_int_array()
count = 0
while A > C * D:
    count += 1
    A += B
    C += D
