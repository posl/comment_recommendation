Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    time = 0
    for a, b in ab:
        time += a
        if time > b:
            print('No')
            break
    else:
        print('Yes')

=======
Suggestion 2

def main():
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += arr[i][0]
        if time > arr[i][1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 3

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = sorted(zip(b, a))
    t = 0
    for i in range(n):
        t += c[i][1]
        if t > c[i][0]:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 4

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))

    AB = sorted(AB, key=lambda x: x[1])
    now = 0
    for a, b in AB:
        now += a
        if now > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += ab[i][0]
        if t > ab[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def main():
    N = int(input())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    t = 0
    for i in range(N):
        t += AB[i][0]
        if t > AB[i][1]:
            print("No")
            break
    else:
        print("Yes")

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    c = sorted(zip(a, b), key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += c[i][0]
        if t > c[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ab = zip(a, b)
    ab = sorted(ab, key=lambda x: x[1])
    a, b = zip(*ab)
    now = 0
    for i in range(n):
        now += a[i]
        if now > b[i]:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def solution():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[1])
    t = 0
    for a, b in ab:
        t += a
        if t > b:
            print('No')
            return
    print('Yes')

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = sorted(zip(b, a))
    t = 0
    for i in c:
        t += i[1]
        if t > i[0]:
            print("No")
            return
    print("Yes")
