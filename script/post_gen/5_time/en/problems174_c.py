Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    x = 7 % k
    for i in range(k):
        if x == 0:
            print(i + 1)
            return
        x = (x * 10 + 7) % k
    print(-1)

main()

=======
Suggestion 2

def main():
    k = int(input())
    seven = 7
    for i in range(k):
        if seven % k == 0:
            print(i+1)
            break
        else:
            seven = seven * 10 + 7
    else:
        print(-1)

=======
Suggestion 3

def main():
    k = int(input())
    a = 7
    for i in range(k):
        if a % k == 0:
            print(i+1)
            return
        a = (a*10 + 7) % k
    print(-1)

=======
Suggestion 4

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        s = 7
        for i in range(k):
            if s % k == 0:
                print(i+1)
                break
            else:
                s = (s * 10 + 7) % k

=======
Suggestion 5

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        x = 7
        for i in range(1, k+1):
            if x % k == 0:
                print(i)
                break
            else:
                x = (x * 10 + 7) % k
        else:
            print(-1)

=======
Suggestion 6

def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    s = 7
    for i in range(K):
        if s % K == 0:
            print(i + 1)
            return
        s = s * 10 + 7
        s %= K
    print(-1)

=======
Suggestion 7

def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        n = 1
        while True:
            if int('7' * n) % k == 0:
                print(n)
                break
            else:
                n += 1

=======
Suggestion 8

def main():
    k = int(input())
    if k%2 == 0 or k%5 == 0:
        print(-1)
    else:
        i = 1
        num = 7%k
        while num != 0:
            num = (num*10 + 7)%k
            i += 1
        print(i)

=======
Suggestion 9

def main():
    K = int(input())
    #print(K)
    #print(type(K))
    #print(7 % K)
    #print(77 % K)
    #print(777 % K)
    #print(7777 % K)
    #print(77777 % K)
    #print(777777 % K)
    #print(7777777 % K)
    #print(77777777 % K)
    #print(777777777 % K)
    #print(7777777777 % K)
    #print(77777777777 % K)
    #print(777777777777 % K)
    #print(7777777777777 % K)
    #print(77777777777777 % K)
    #print(777777777777777 % K)
    #print(7777777777777777 % K)
    #print(77777777777777777 % K)
    #print(777777777777777777 % K)
    #print(7777777777777777777 % K)
    #print(77777777777777777777 % K)
    #print(777777777777777777777 % K)
    #print(7777777777777777777777 % K)
    #print(77777777777777777777777 % K)
    #print(777777777777777777777777 % K)
    #print(7777777777777777777777777 % K)
    #print(77777777777777777777777777 % K)
    #print(777777777777777777777777777 % K)
    #print(7777777777777777777777777777 % K)
    #print(77777777777777777777777777777 % K)

=======
Suggestion 10

def solution(k):
    if k%2 == 0 or k%5 == 0:
        return -1
    else:
        if k == 1:
            return 1
        else:
            n = 1
            x = 7
            while True:
                if x%k == 0:
                    return n
                else:
                    n += 1
                    x = x*10 + 7
    return -1
