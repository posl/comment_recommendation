Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 1:
                flag = False
                break
            a[i] //= 2
        if flag:
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 2

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                flag = False
                break
        if flag:
            ans += 1
        else:
            break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            exit()
    print(ans)

=======
Suggestion 3

def solve(n, a):
    count = 0
    while True:
        if all([i%2==0 for i in a]):
            a = [i/2 for i in a]
            count += 1
        else:
            break
    while True:
        if all([i%3==0 for i in a]):
            a = [i/3 for i in a]
            count += 1
        else:
            break
    if all([i==a[0] for i in a]):
        return count
    else:
        return -1

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            else:
                break
        else:
            count += 1
            continue
        break
    print(count)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        odd = False
        for i in range(N):
            if A[i] % 2 != 0:
                odd = True
        if odd:
            break
        for i in range(N):
            A[i] = A[i] // 2
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                flag = False
        if flag == False:
            break
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] // 2
            else:
                flag = False
                break
        if flag:
            count += 1
        else:
            break

    print(count)

=======
Suggestion 8

def count_operation(a):
    count = 0
    while True:
        if all([x % 2 == 0 for x in a]):
            a = [x / 2 for x in a]
            count += 1
        elif all([x % 3 == 0 for x in a]):
            a = [x / 3 for x in a]
            count += 1
        elif all([x == a[0] for x in a]):
            return count
        else:
            return -1

=======
Suggestion 9

def solve(n, a):
    if sum(a) % n != 0:
        return -1
    target = sum(a) // n
    cnt = 0
    for i in range(n):
        if a[i] % 2 == 0:
            while a[i] % 2 == 0:
                a[i] //= 2
                cnt += 1
        if a[i] % 3 == 0:
            while a[i] % 3 == 0:
                a[i] //= 3
                cnt += 1
    return cnt

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = False
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
                flag = True
                ans += 1
        if flag:
            continue
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] //= 3
                flag = True
                ans += 1
        if flag:
            continue
        break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            return
    print(ans)
