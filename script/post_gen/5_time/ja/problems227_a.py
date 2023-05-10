Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k, a = map(int, input().split())
    print((k + a - 1) % n + 1)

=======
Suggestion 2

def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        count = 0
        while k > n:
            k -= n
            count += 1
        if k <= n:
            if k <= a:
                print(k + count * n)
            else:
                print(k + count * n + 1)

=======
Suggestion 3

def main():
    n,k,a = map(int,input().split())
    print((k-1+n-a)%n+1)

=======
Suggestion 4

def main():
    N, K, A = map(int, input().split())
    print((K - 1 + A - 1) % N + 1)

=======
Suggestion 5

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        if a == 1:
            print(n)
        else:
            print(a - 1)
    else:
        if a == 1:
            print(k % n)
        else:
            if k % n + a - 1 <= n:
                print(k % n + a - 1)
            else:
                print(k % n + a - n - 1)

=======
Suggestion 6

def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        k = k - n
        while k > 0:
            a += 1
            k -= 1
            if a == n + 1:
                a = 1
        print(a)

=======
Suggestion 7

def main():
    n,k,a = map(int,input().split())
    #print(n,k,a)
    #n,k,a = 3,3,2
    #n,k,a = 1,100,1
    #n,k,a = 3,14,2
    if k <= n:
        print(k)
    else:
        k = k - n
        a = a + k
        if a > n:
            a = a - n
        print(a)

=======
Suggestion 8

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print(a + k % n - 1 if a + k % n <= n else a + k % n - n)

=======
Suggestion 9

def main():
    N, K, A = map(int, input().split())
    if K <= N:
        print(K + A - 1)
    else:
        print(K % N + A - 1)
