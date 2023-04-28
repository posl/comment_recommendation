Synthesizing 10/10 solutions

=======
Suggestion 1

def swap(s, a, b):
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 2

def swap(s, a, b):
    if a < b:
        return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]
    else:
        return s[:b-1] + s[a-1] + s[b:a-1] + s[b-1] + s[a:]

N = int(input())
S = input()
Q = int(input())

s1 = S[:N]
s2 = S[N:]

for i in range(Q):
    T,A,B = map(int, input().split())
    if T == 1:
        if A <= N and B <= N:
            s1 = swap(s1, A, B)
        elif N < A and N < B:
            s2 = swap(s2, A-N, B-N)
        else:
            s1, s2 = s2, s1
    else:
        s1, s2 = s2, s1

print(s1 + s2)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    q = int(input())
    s = list(s)
    for i in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            s[a-1], s[b-1] = s[b-1], s[a-1]
        else:
            s[:n], s[n:] = s[n:], s[:n]
    print(''.join(s))

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    q = int(input())
    l = list(s[:n])
    r = list(s[n:])
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            if a <= n and b <= n:
                l[a-1], l[b-1] = l[b-1], l[a-1]
            elif a <= n and b > n:
                l[a-1], r[b-n-1] = r[b-n-1], l[a-1]
            elif a > n and b > n:
                r[a-n-1], r[b-n-1] = r[b-n-1], r[a-n-1]
        elif t == 2:
            l, r = r, l
    print(''.join(l + r))

=======
Suggestion 5

def swap(s, i, j):
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

=======
Suggestion 6

def swap(s, a, b):
    if a == b:
        return s
    if a > b:
        a, b = b, a
    return s[:a-1] + s[b-1] + s[a:b-1] + s[a-1] + s[b:]

=======
Suggestion 7

def swap(s, a, b):
    a -= 1
    b -= 1
    if a < len(s)/2 and b < len(s)/2:
        s[a], s[b] = s[b], s[a]
    elif a >= len(s)/2 and b >= len(s)/2:
        s[a], s[b] = s[b], s[a]
    else:
        if a >= len(s)/2:
            a -= len(s)/2
            b += len(s)/2
        else:
            a += len(s)/2
            b -= len(s)/2
        s[a], s[b] = s[b], s[a]
    return s

n = input()
s = list(raw_input())
q = input()

for i in xrange(q):
    t, a, b = map(int, raw_input().split())
    if t == 1:
        s = swap(s, a, b)
    else:
        s[:n], s[n:] = s[n:], s[:n]
print "".join(s)

=======
Suggestion 8

def flip(s):
    return s[N:] + s[:N]

N = int(input())
S = input()
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

for q in query:
    if q[0] == 1:
        A, B = q[1]-1, q[2]-1
        S = S[:A] + S[B] + S[A+1:B] + S[A] + S[B+1:]
    else:
        S = flip(S)

print(S)

=======
Suggestion 9

def flip(S):
    n = len(S)
    return S[n:]+S[:n]

N = int(input())
S = input()
Q = int(input())

flipped = False

for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if flipped:
            A = (A + N) % (2*N)
            B = (B + N) % (2*N)
        S = S[:A-1] + S[B-1] + S[A:B-1] + S[A-1] + S[B:]
    else:
        flipped = not flipped

=======
Suggestion 10

def swap(a, b):
    return b, a
