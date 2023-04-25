Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    num = 7
    for i in range(1, k+1):
        if num % k == 0:
            print(i)
            return
        num = (num * 10 + 7) % k
    print(-1)

=======
Suggestion 2

def main():
    k = int(input())
    a = 7
    for i in range(1, k+1):
        if a % k == 0:
            print(i)
            return
        a = (a * 10 + 7) % k
    print(-1)

=======
Suggestion 3

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    num = 7
    for i in range(1, k + 1):
        if num % k == 0:
            print(i)
            return
        num = num * 10 + 7
    print(-1)
    return

=======
Suggestion 4

def main():
    k = int(input())
    r = 7
    for i in range(k):
        if r % k == 0:
            print(i+1)
            return
        r = (r*10+7) % k
    print(-1)

=======
Suggestion 5

def main():
    K = int(input())
    N = 7
    for i in range(1, K+1):
        if N % K == 0:
            print(i)
            break
        N = N * 10 + 7
    else:
        print(-1)

=======
Suggestion 6

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    else:
        num = 7
        for i in range(1, K + 1):
            if num % K == 0:
                print(i)
                return
            num = num * 10 + 7
        print(-1)

=======
Suggestion 7

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    else:
        i = 1
        n = 7
        while n % k != 0:
            n = (n * 10 + 7) % k
            i += 1
        print(i)

=======
Suggestion 8

def main():
    k = int(input().rstrip())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    r = 1
    for i in range(1, k+1):
        r = (r * 10 + 7) % k
        if r == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 9

def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    else:
        i = 1
        while True:
            if int(str(7) * i) % K == 0:
                print(i)
                return
            else:
                i += 1

=======
Suggestion 10

def main():
    # input
    k = int(input())
    # solve
    if k % 2 == 0:
        print(-1)
    else:
        seven = 7
        for i in range(1, 10**6+1):
            if seven % k == 0:
                print(i)
                break
            else:
                seven = seven * 10 + 7
