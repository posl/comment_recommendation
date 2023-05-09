Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    c = input()
    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
    for i in range(r):
        if c[i] == 'W':
            w += 1
    print(w)

=======
Suggestion 2

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
    else:
        a = 0
        b = r-1
        while a < b:
            if c[a] == 'W':
                while c[b] == 'W':
                    b -= 1
                c = c[:a] + 'R' + c[a+1:b] + 'W' + c[b+1:]
            a += 1
        print(c.count('W'))
    return 0

=======
Suggestion 3

def main():
    n = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    ans = 0
    for i in range(r):
        if c[i] == 'W':
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    c = input()

    r = 0
    w = 0
    for i in range(N):
        if c[i] == 'R':
            r += 1
        else:
            w += 1

    if r == 0 or w == 0:
        print(0)
        return

    r_ = 0
    w_ = 0
    for i in range(N):
        if c[i] == 'R':
            r_ += 1
        else:
            w_ += 1
        if r_ == r and w_ == w:
            print(i + 1)
            return

    print(r)

=======
Suggestion 5

def main():
    N = int(input())
    c = input()
    r = c.count('R')
    w = c.count('W')
    if r == 0 or w == 0:
        print(0)
    else:
        print(min(r,c.rfind('R')+1,w,c.find('W')+1))

=======
Suggestion 6

def solve():
    N = int(input())
    C = input()
    R = C.count('R')
    W = C.count('W')
    if R == 0 or W == 0:
        print(0)
        return
    if C[0] == 'R':
        print(C[:R].count('W'))
    else:
        print(C[R:].count('R'))

=======
Suggestion 7

def solve(N, C):
    W = 0
    for i in range(N):
        if C[i] == "W":
            W += 1
    if W == 0 or W == N:
        return 0
    l = 0
    r = N - 1
    ans = 0
    while l < r:
        if C[l] == "W" and C[r] == "R":
            ans += 1
            l += 1
            r -= 1
        elif C[l] == "W":
            r -= 1
        elif C[r] == "R":
            l += 1
        else:
            l += 1
            r -= 1
    return ans


N = int(input())
C = input()
print(solve(N, C))

=======
Suggestion 8

def main():
    n = int(input())
    c = input()
    w = c.count('W')
    r = c.count('R')
    ans = min(w, r)
    w = 0
    r = 0
    for i in range(n):
        if c[i] == 'W':
            w += 1
        else:
            r += 1
        ans = min(ans, max(w, r))
    print(ans)

=======
Suggestion 9

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

=======
Suggestion 10

def main():
    N = int(input())
    c = input()
    c_list = list(c)
    c_list_left = []
    c_list_right = []
    for i in range(N):
        c_list_left.append(c_list[i])
        c_list_right.append(c_list[N-i-1])
    for i in range(N):
        if c_list_left[i] == 'R':
            break
    for j in range(N):
        if c_list_right[j] == 'W':
            break
    if i < j:
        print(j-i)
    else:
        print(0)
