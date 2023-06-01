Synthesizing 10/10 solutions

=======
Suggestion 1

def divide2(num):
    return num/2

=======
Suggestion 2

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 1:
                return ans
        for i in range(N):
            a[i] //= 2
        ans += 1

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1
    print(ans)

=======
Suggestion 4

def div2(num):
    count = 0
    while True:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            break
    return count

N = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(N):
    count += div2(a[i])
print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] /= 2
            cnt += 1
    print(cnt)

=======
Suggestion 7

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 1:
                print(ans)
                return
            else:
                a[i] //= 2
        ans += 1

=======
Suggestion 8

def get_num(n):
    if n%2 == 0:
        return n/2
    else:
        return n*3

=======
Suggestion 9

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            ans += 1
    print(ans)
