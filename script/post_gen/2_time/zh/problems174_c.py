Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    k = int(input())
    a = 7
    for i in range(1, k+1):
        if a % k == 0:
            print(i)
            return
        a = a * 10 + 7
    print(-1)

=======
Suggestion 2

def main():
    k = int(input())
    s = 7
    for i in range(1, k+1):
        if s % k == 0:
            print(i)
            return
        s = (s * 10 + 7) % k
    print(-1)

=======
Suggestion 3

def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return
    count = 0
    for i in range(1, k):
        count = count * 10 + 7
        count %= k
        if count == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 4

def problem174_c():
    pass

=======
Suggestion 5

def main():
    a = int(input())
    x = 7
    for i in range(1, a+1):
        if x % a == 0:
            print(i)
            break
        x = x*10 + 7
    else:
        print(-1)

=======
Suggestion 6

def getK(k):
    if k%2==0 or k%5==0:
        return -1
    else:
        x=0
        for i in range(1,k+1):
            x=x*10+7
            if x%k==0:
                return i
        return -1

=======
Suggestion 7

def main():
    k = int(input())
    if k%2 == 0:
        print(-1)
    else:
        cnt = 0
        while True:
            cnt += 1
            if int('7'*cnt)%k == 0:
                print(cnt)
                break

=======
Suggestion 8

def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        return

    i = 1
    num = 7
    while num % k != 0:
        num = num * 10 + 7
        num %= k
        i += 1

    print(i)

=======
Suggestion 9

def check(k):
    num = 0
    for i in range(1000000):
        num = num * 10 + 7
        num %= k
        if num == 0:
            return i + 1
    return -1

k = int(input())
print(check(k))

=======
Suggestion 10

def problem174_c():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
    else:
        x = 7
        for i in range(1, k + 1):
            if x % k == 0:
                print(i)
                break
            else:
                x = x * 10 + 7
        else:
            print(-1)
