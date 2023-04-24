Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    n = 7
    for i in range(1, k+1):
        if n % k == 0:
            print(i)
            return
        n = (n * 10 + 7) % k
    print(-1)

=======
Suggestion 2

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        x = 7 % k
        for i in range(k):
            if x == 0:
                print(i + 1)
                break
            x = (x * 10 + 7) % k

=======
Suggestion 3

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
    else:
        count = 1
        num = 7
        while num % K != 0:
            num = (num * 10 + 7) % K
            count += 1
        print(count)
    return

=======
Suggestion 4

def main():
    k = int(input())
    if k%2 == 0 or k%5 == 0:
        print(-1)
        return
    ans = 0
    for i in range(1,k+1):
        ans = (ans*10+7) % k
        if ans == 0:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 5

def main():
    n = int(input())
    x = 7
    for i in range(1, n+1):
        if x % n == 0:
            print(i)
            exit()
        else:
            x = x*10 + 7
    print(-1)

=======
Suggestion 6

def main():
    K = int(input())
    if K%2 == 0 or K%5 == 0:
        print(-1)
        return
    count = 1
    num = 7
    while num%K != 0:
        num = (num*10 + 7)%K
        count += 1
    print(count)

=======
Suggestion 7

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    ans = 1
    s = 7
    while True:
        if s % k == 0:
            print(ans)
            return
        s = (s * 10 + 7) % k
        ans += 1

=======
Suggestion 8

def main():
    n = int(input())
    for i in range(1, n+1):
        if (7 * i) % n == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 9

def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
    else:
        mod = 7
        for i in range(10**6):
            if mod % k == 0:
                print(i+1)
                break
            mod = mod * 10 + 7
        else:
            print(-1)

=======
Suggestion 10

def seven_multiple(K):
    i = 0
    s = 0
    while True:
        i += 1
        s = (s*10 + 7) % K
        if s == 0:
            return i
        if i == K:
            return -1

K = int(input())
print(seven_multiple(K))
