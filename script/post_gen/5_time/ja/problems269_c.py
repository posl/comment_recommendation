Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    n = int(input())
    ans = []
    for i in range(0, 61):
        if n & (1 << i) != 0:
            ans.append(i)
    for i in range(0, len(ans)):
        print(1 << ans[i])

=======
Suggestion 2

def main():
    N = int(input())
    ans = []
    for i in range(1<<15):
        x = 0
        for j in range(15):
            if i & (1<<j):
                x += 2**j
        if x <= N:
            ans.append(x)
    print(*ans, sep="\n")

=======
Suggestion 3

def main():
    n = int(input())
    l = []
    for i in range(60):
        if n & (1 << i):
            l.append(i)
    ans = []
    for i in range(1 << len(l)):
        x = 0
        for j in range(len(l)):
            if i & (1 << j):
                x += 1 << l[j]
        if x <= n:
            ans.append(x)
    print(*ans, sep="\n")

=======
Suggestion 4

def main():
    N = int(input())
    ans = []
    for i in range(0, 2**15):
        if i & N == i:
            ans.append(i)
    print(*ans, sep='\n')

=======
Suggestion 5

def main():
    n = int(input())
    ans = []
    for i in range(1 << 15):
        x = 0
        for j in range(15):
            if i & (1 << j):
                x += 2 ** j
        if x <= n and x & n == x:
            ans.append(x)
    print(*ans, sep='\n')

=======
Suggestion 6

def main():
    n = int(input())
    ans = []
    for i in range(2**15):
        if n & i == i:
            ans.append(i)
    print("\n".join(map(str, ans)))

=======
Suggestion 7

def main():
    n = int(input())
    l = []
    for i in range(1, 2**16):
        if n & i == i:
            l.append(i)
    l.sort()
    for i in l:
        print(i)

=======
Suggestion 8

def solve():
    n = int(input())
    if n == 0:
        print(0)
        return
    ans = []
    for i in range(1, 60):
        if n & (1 << i):
            ans.append(i)
    ans.append(0)
    ans.sort()
    for i in ans:
        print(1 << i)

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(2**15):
        x = 0
        for j in range(15):
            if i>>j&1:
                x += 2**j
        if x&n == x:
            print(x)

=======
Suggestion 10

def main():
    #n = int(input())
    n = 576461302059761664
    #n = 11
    #n = 0
    #n = 576461302059761664
    #n = 576461302059237376
    #n = 576460752303947776
    #n = 576460752303423488
    #n = 549756338176
    #n = 549755813888
    #n = 524288
    #n = 0
    #n = 11
    #n = 576461302059761664
    #n = 576461302059237376
    #n = 576460752303947776
    #n = 576460752303423488
    #n = 549756338176
    #n = 549755813888
    #n = 524288
    #n = 0
    #n = 11
    #n = 576461302059761664
    #n = 576461302059237376
    #n = 576460752303947776
    #n = 576460752303423488
    #n = 549756338176
    #n = 549755813888
    #n = 524288
    #n = 0
    #n = 11
    #n = 576461302059761664
    #n = 576461302059237376
    #n = 576460752303947776
    #n = 576460752303423488
    #n = 549756338176
    #n = 549755813888
    #n = 524288
    #n = 0
    #n = 11
    #n = 576461302059761664
    #n = 576461302059237376
    #n = 576460752303947776
    #n = 576460752303423488
    #n = 549756338176
    #n = 549755813888
    #n = 524288
    #n = 0
    #n = 11
    #n = 576461302059761664
    #n =
