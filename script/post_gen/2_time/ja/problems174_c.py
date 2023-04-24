Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    a = 7 % K
    for i in range(1, K+1):
        if a == 0:
            print(i)
            return
        a = (a*10 + 7) % K
    print(-1)

=======
Suggestion 2

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        n = 1
        while n % K != 0:
            n = n * 10 + 7
            n %= K
        print(len(str(n)))

=======
Suggestion 3

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    n = 7
    for i in range(1, K+1):
        if n % K == 0:
            print(i)
            return
        n = (n * 10 + 7) % K

=======
Suggestion 4

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    x = 0
    for i in range(1, K + 1):
        x = x * 10 + 7
        x %= K
        if x == 0:
            print(i)
            return

=======
Suggestion 5

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    n = 1
    while 7 % k != 0:
        n += 1
        7 = 7 * 10 + 7
    print(n)

=======
Suggestion 6

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    else:
        num = 7
        cnt = 1
        while num % K != 0:
            num = num * 10 + 7
            cnt += 1
        print(cnt)

=======
Suggestion 7

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    n = 1
    for i in range(1, K + 1):
        n = (n * 10 + 7) % K
        if n == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 8

def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
    else:
        ans = 7 % k
        for i in range(1, 10**6):
            if ans == 0:
                print(i)
                exit()
            ans = (ans * 10 + 7) % k
        print(-1)

=======
Suggestion 9

def main():
    K = int(input())
    n = 0
    for i in range(1, K+1):
        n = n*10 + 7
        n = n % K
        if n == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 10

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    else:
        i = 1
        while i * 7 % K != 0:
            i += 1
        print(i)
