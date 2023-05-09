Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    s = 0
    for i in range(n):
        s += a[i]/b[i]
    s /= 2
    t = 0
    for i in range(n-1, -1, -1):
        if s >= a[i]/b[i]:
            t += a[i]
            s -= a[i]/b[i]
        else:
            t += s*b[i]
            break
    print(t)

main()

=======
Suggestion 2

def get_input():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, A, B

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = [int(i) for i in input().split()]
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")
    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

    #print(A)
    #print(B)
    #print(N)
    #print("Hello World")

=======
Suggestion 4

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    t = 0
    for A, B in AB:
        t += A / B
    t /= 2
    x = 0
    for A, B in AB:
        if t > A / B:
            t -= A / B
            x += A
        else:
            x += B * t
            break
    print(x)

=======
Suggestion 5

def solve():
    N = int(input())
    AB = [list(map(int, input().split())) for i in range(N)]
    s = 0
    for i in range(N):
        s += AB[i][0]/AB[i][1]
    s /= 2
    t = 0
    for i in range(N):
        t += AB[i][0]/AB[i][1]
        if t>=s:
            print(s)
            break
        else:
            continue

=======
Suggestion 6

def solve():
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int,input().split())

    total = 0
    for i in range(n):
        total += a[i]/b[i]

    half = total/2
    time = 0
    for i in range(n):
        time += a[i]/b[i]
        if time >= half:
            print(time - (time - half)*2)
            break

=======
Suggestion 7

def main():
    # input
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # compute
    left = 0
    right = 0
    for a, b in AB:
        left += a / b
        right += a
    # output
    print(left / 2 + right / 2)

=======
Suggestion 8

def main():
    import sys
    import math
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[0])
    a_b.sort(key=lambda x: x[1], reverse=True)
    a = [x[0] for x in a_b]
    b = [x[1] for x in a_b]
    sum_a = sum(a)
    sum_b = sum(b)
    sum_a_b = 0
    for i in range(n):
        sum_a_b += a[i]
        sum_b -= b[i]
        if sum_a_b > sum_b:
            print(sum_a_b - a[i] + (sum_b - (sum_a_b - a[i]))/2)
            sys.exit()

=======
Suggestion 9

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    maxt = 0
    for i in range(n):
        maxt = max(maxt, ab[i][0]/ab[i][1])
    print(sum(map(lambda x: x[0], ab)) - maxt/2)

=======
Suggestion 10

def main():
    N = int(input())
    A_B = []
    for i in range(N):
        A_B.append(list(map(int,input().split())))
    #print(A_B)
    A_B.sort(key=lambda x:x[0])
    #print(A_B)
    total_time = 0
    for i in range(N):
        total_time += A_B[i][0]/A_B[i][1]
    #print(total_time)
    half_time = total_time/2
    #print(half_time)
    distance = 0
    for i in range(N):
        if half_time <= A_B[i][0]/A_B[i][1]:
            distance += half_time*A_B[i][1]
            break
        else:
            distance += A_B[i][0]
            half_time -= A_B[i][0]/A_B[i][1]
    print(distance)
