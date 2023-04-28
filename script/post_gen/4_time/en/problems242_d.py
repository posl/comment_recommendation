Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    q = int(input())
    a = s.count('A')
    b = s.count('B')
    c = s.count('C')
    for _ in range(q):
        t, k = map(int, input().split())
        t %= 3
        if t == 0:
            if k <= a:
                print('A')
            elif k <= a + b:
                print('B')
            else:
                print('C')
        elif t == 1:
            if k <= b:
                print('B')
            elif k <= a + b:
                print('A')
            else:
                print('C')
        else:
            if k <= c:
                print('C')
            elif k <= a + c:
                print('A')
            else:
                print('B')

=======
Suggestion 2

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        if t == 0:
            print(S[k - 1])
        else:
            if S[k - 1] == "A":
                print("B")
            elif S[k - 1] == "B":
                print("C")
            else:
                print("A")

=======
Suggestion 3

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t % 3 == 1:
            if k % 3 == 1:
                print(s[0])
            elif k % 3 == 2:
                print(s[1])
            else:
                print(s[2])
        elif t % 3 == 2:
            if k % 3 == 1:
                print(s[1])
            elif k % 3 == 2:
                print(s[2])
            else:
                print(s[0])
        else:
            if k % 3 == 1:
                print(s[2])
            elif k % 3 == 2:
                print(s[0])
            else:
                print(s[1])

=======
Suggestion 4

def main():
    S = input()
    Q = int(input())
    for q in range(Q):
        t, k = map(int, input().split())
        if t == 0:
            print(S[k - 1])
        else:
            if k % len(S) == 0:
                print(S[-1])
            else:
                print(S[k % len(S) - 1])

=======
Suggestion 5

def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        k -= 1
        l = len(S)
        while t > 0:
            if k < l:
                if S[k] != 'A':
                    if S[k] == 'B':
                        if t % 3 == 1:
                            print('A')
                        elif t % 3 == 2:
                            print('C')
                        else:
                            print('B')
                    else:
                        if t % 3 == 1:
                            print('C')
                        elif t % 3 == 2:
                            print('B')
                        else:
                            print('A')
                    break
            else:
                k = k % l
                if t % 2 == 1:
                    if S[k] == 'A':
                        print('B')
                    elif S[k] == 'B':
                        print('C')
                    else:
                        print('A')
                    break
                else:
                    if S[k] == 'A':
                        print('C')
                    elif S[k] == 'B':
                        print('A')
                    else:
                        print('B')
                    break

=======
Suggestion 6

def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        k -= 1
        while t:
            if S[k] == 'A':
                k = k % (2 ** t)
            elif S[k] == 'B':
                k = (2 ** t) + k % (2 ** t)
            elif S[k] == 'C':
                k = (4 ** t) + k % (2 ** t)
            t -= 1
        print(S[k])

=======
Suggestion 7

def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        while t > 0:
            if k % 2 == 1:
                k = (k + 1) // 2
            else:
                k = (k + 1) // 2 + len(S) // 2
            t -= 1
        print(S[k - 1])

=======
Suggestion 8

def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        k -= 1
        l = len(s)
        if t % 3 == 1:
            print(s[k % l])
        elif t % 3 == 2:
            print(s[(k + l // 3) % l])
        else:
            print(s[(k + 2 * l // 3) % l])

=======
Suggestion 9

def f(s, t):
    if t == 0:
        return s
    if t % 2 == 0:
        return f(s, t // 2) + f(s, t // 2)
    else:
        return f(s, t // 2) + f(s, t // 2) + s

s = input()
q = int(input())
t = [0] * q
k = [0] * q
for i in range(q):
    t[i], k[i] = map(int, input().split())
    print(f(s, t[i])[k[i] - 1])

=======
Suggestion 10

def main():
    s = input()
    q = int(input())

    # 0: ABC, 1: BCA, 2: CAB
    t = [0, 1, 2]
    for _ in range(q):
        ti, ki = map(int, input().split())
        ti = ti % 3
        ki -= 1
        if t[ti] == 0:
            print(s[ki])
        elif t[ti] == 1:
            print('B' if s[ki] == 'A' else 'C' if s[ki] == 'B' else 'A')
        else:
            print('C' if s[ki] == 'A' else 'A' if s[ki] == 'B' else 'B')
