Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in reversed(range(1, N + 1)):
        s = sum(B[i::i]) % 2
        if s != A[i - 1]:
            B[i] = 1
    M = sum(B)
    print(M)
    if M > 0:
        print(' '.join(map(str, [i for i, b in enumerate(B) if b])))

solve()

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int,input().split()))
    b = [0]*N
    c = [0]*N
    for i in range(N):
        if a[i] == 1:
            if i+1 > N//2:
                b[i] = 1
            else:
                c[i] = 1
    if sum(b) == 0:
        print(0)
    elif sum(b) > sum(c):
        print(sum(b))
        for i in range(N):
            if b[i] == 1:
                print(i+1,end=' ')
        print('')
    else:
        print(sum(c))
        for i in range(N):
            if c[i] == 1:
                print(i+1,end=' ')
        print('')

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N, 0, -1):
        if a[i-1]:
            ans.append(i)
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    a[j-1] = 1 - a[j-1]
                    if j != i//j:
                        a[i//j-1] = 1 - a[i//j-1]
    M = sum(a)
    print(M)
    if M:
        print(*ans)

=======
Suggestion 5

def solve(n, a):
    if n == 1:
        if a[0] == 1:
            return [1]
        else:
            return [-1]
    if n == 2:
        if a[0] == 0 and a[1] == 0:
            return [0]
        elif a[0] == 1 and a[1] == 1:
            return [1, 2]
        else:
            return [-1]
    if n == 3:
        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            return [0]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0:
            return [1]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0:
            return [2]
        elif a[0] == 0 and a[1] == 0 and a[2] == 1:
            return [3]
        elif a[0] == 1 and a[1] == 1 and a[2] == 0:
            return [1, 2]
        elif a[0] == 0 and a[1] == 1 and a[2] == 1:
            return [2, 3]
        elif a[0] == 1 and a[1] == 0 and a[2] == 1:
            return [1, 3]
        elif a[0] == 1 and a[1] == 1 and a[2] == 1:
            return [1, 2, 3]
        else:
            return [-1]
    if n == 4:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            return [0]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            return [1]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 0:
            return [2

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        if a[i] == 1:
            b.append(i+1)
    m = len(b)
    if m == 0:
        print(0)
        return
    if m == 1:
        print(1)
        print(b[0])
        return
    if m == 2:
        print(2)
        print(b[0], b[1])
        return
    print(m)
    for i in range(m):
        print(b[i], end=' ')
    print()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        j = i * 2
        t = 0
        while j <= n:
            t += b[j]
            j += i
        if a[i - 1] != t % 2:
            b[i] = 1
    print(sum(b))
    for i in range(1, n + 1):
        if b[i] == 1:
            print(i, end=' ')
    print()

=======
Suggestion 8

def problems134_d():
    pass

=======
Suggestion 9

def solve(n, a):
    b = [0] * n
    for i in range(n):
        b[i] = 1 if a[i] else 0
    return b

=======
Suggestion 10

def get_input():
    N = int(raw_input())
    a = map(int, raw_input().split())
    return N, a
