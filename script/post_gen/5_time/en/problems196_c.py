Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                count += 1
    print(count)
    return

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    # input
    N = int(input())
    # compute
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                ans += 1
    # output
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                result += 1
    print(result)

=======
Suggestion 6

def main():
    N = input()
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))/2] == str(i)[len(str(i))/2:]:
                count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        a = str(i)
        if len(a) % 2 == 0:
            if a[:len(a)//2] == a[len(a)//2:]:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    s = str(N)
    l = len(s)
    if l == 1:
        print(0)
    else:
        if l % 2 == 0:
            print(int(s[:l//2]) - 1)
        else:
            print(int(s[:l//2]))

=======
Suggestion 9

def solve():
    n = int(input())
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            p = 10 * i + j
            q = 10 * j + i
            if p <= n:
                ans += 1
            if q <= n:
                ans += 1
    print(ans)
