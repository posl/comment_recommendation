Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def countop(a):
    count = 0
    for i in a:
        while i % 2 == 0:
            i /= 2
            count += 1
    return count

=======
Suggestion 2

def solve(N, a):
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    return count

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] /= 2
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    #print("start")
    N = int(input())
    a = list(map(int,input().split()))
    #print(N)
    #print(a)
    #print("end")
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
    print(count)
    return 0

=======
Suggestion 6

def func():
    N = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] /= 2
            count += 1
    print(count)

=======
Suggestion 7

def count2(n):
    count = 0
    while n % 2 == 0:
        n = n / 2
        count += 1
    return count

=======
Suggestion 8

def solution(n, a_list):
    count = 0
    while True:
        flag = False
        for i in range(0, n):
            if a_list[i] % 2 == 0:
                a_list[i] = a_list[i] / 2
                flag = True
        if flag:
            count += 1
        else:
            break
    return count

=======
Suggestion 9

def main():
    # N = int(input())
    # a = list(map(int, input().split()))
    N = 3
    a = [5, 2, 4]
    cnt = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            cnt += 1
    print(cnt)
