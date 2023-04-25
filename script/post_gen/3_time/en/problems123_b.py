Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A%10, B%10, C%10, D%10, E%10)
    if min_time == 0:
        print(A+B+C+D+E)
    else:
        print(A+B+C+D+E-10+min_time)

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10 == 0:
        a1 = a
    else:
        a1 = a + (10 - a%10)
    if b%10 == 0:
        b1 = b
    else:
        b1 = b + (10 - b%10)
    if c%10 == 0:
        c1 = c
    else:
        c1 = c + (10 - c%10)
    if d%10 == 0:
        d1 = d
    else:
        d1 = d + (10 - d%10)
    if e%10 == 0:
        e1 = e
    else:
        e1 = e + (10 - e%10)
    print(a1 + b1 + c1 + d1 + e1 - max(a1,b1,c1,d1,e1))

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(min((A+9)//10*10, (B+9)//10*10, (C+9)//10*10, (D+9)//10*10, (E+9)//10*10) + max(A, B, C, D, E))

=======
Suggestion 4

def main():
    # Get input here
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    # Calculate result here
    result = 0
    if a%10 != 0:
        a += 10 - a%10
    if b%10 != 0:
        b += 10 - b%10
    if c%10 != 0:
        c += 10 - c%10
    if d%10 != 0:
        d += 10 - d%10
    if e%10 != 0:
        e += 10 - e%10

    result = a + b + c + d + e

    # Print result here
    print(result)

main()

=======
Suggestion 5

def main():
  #!/usr/bin/env python3
  # -*- coding: utf-8 -*-
  A = int(input())
  B = int(input())
  C = int(input())
  D = int(input())
  E = int(input())
  #prin

=======
Suggestion 6

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(max([A, B, C, D, E]))

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    min_time = min(a,b,c,d,e)
    time = 0
    if a % 10 != 0:
        time += (a//10 + 1) * 10
    else:
        time += a
    if b % 10 != 0:
        time += (b//10 + 1) * 10
    else:
        time += b
    if c % 10 != 0:
        time += (c//10 + 1) * 10
    else:
        time += c
    if d % 10 != 0:
        time += (d//10 + 1) * 10
    else:
        time += d
    if e % 10 != 0:
        time += (e//10 + 1) * 10
    else:
        time += e
    time -= 10
    print(time)

=======
Suggestion 8

def main():
    # input
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    # compute
    ans = 0
    if A%10 != 0:
        A = ((A//10)+1)*10
    if B%10 != 0:
        B = ((B//10)+1)*10
    if C%10 != 0:
        C = ((C//10)+1)*10
    if D%10 != 0:
        D = ((D//10)+1)*10
    if E%10 != 0:
        E = ((E//10)+1)*10

    ans = A + B + C + D + E

    # output
    print(ans)

=======
Suggestion 9

def calculate_wait_time(orders):
    max_time = 0
    for order in orders:
        order_time = (order // 10 + 1) * 10
        if order_time > max_time:
            max_time = order_time
    return max_time

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
