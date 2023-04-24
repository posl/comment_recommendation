Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    x = 7
    for i in range(K):
        if x % K == 0:
            print(i + 1)
            return
        x = x * 10 + 7
    print(-1)
    return

=======
Suggestion 2

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return

    ans = 1
    n = 7 % K
    while n != 0:
        n = (n * 10 + 7) % K
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        n = 1
        while 7 % K != 0:
            n += 1
            7 %= K
            7 *= 10
            7 += 7
        print(n)

=======
Suggestion 4

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    i = 1
    while True:
        if i % K == 0:
            print(i)
            return
        i += 1

=======
Suggestion 5

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return

    N = 7 % K
    count = 1
    while N != 0:
        N = (N * 10 + 7) % K
        count += 1
    print(count)

=======
Suggestion 6

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return

    i = 1
    mod = 7 % K
    while mod != 0:
        mod = (mod * 10 + 7) % K
        i += 1
    print(i)

=======
Suggestion 7

def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
    else:
        ans = 7 % K
        for i in range(1, 10**6):
            if ans == 0:
                print(i)
                break
            else:
                ans = (ans * 10 + 7) % K
        else:
            print(-1)

=======
Suggestion 8

def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    else:
        n = 7
        for i in range(1, 10**6):
            if n % K == 0:
                print(i)
                return
            else:
                n = n * 10 + 7
        print(-1)
        return

=======
Suggestion 9

def main():
    K = int(input())
    #K = 999983
    num = 7
    for i in range(1, K+1):
        if num % K == 0:
            print(i)
            return
        num = (num * 10 + 7) % K
    print(-1)
