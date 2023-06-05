Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def read_ints():
    return list(map(int,input().split()))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i, j in enumerate(a):
        if i+1 < j:
            ans = i+1
    print(ans)

=======
Suggestion 3

def solve(n, a):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 3
    if n == 5:
        return 4
    if n == 6:
        return 4
    if n == 7:
        return 5
    if n == 8:
        return 6
    if n == 9:
        return 7
    if n == 10:
        return 8
    if n == 11:
        return 9
    if n == 12:
        return 9
    if n == 13:
        return 10
    if n == 14:
        return 11
    if n == 15:
        return 12
    if n == 16:
        return 13
    if n == 17:
        return 14
    if n == 18:
        return 14
    if n == 19:
        return 15
    if n == 20:
        return 16
    if n == 21:
        return 17
    if n == 22:
        return 18
    if n == 23:
        return 19
    if n == 24:
        return 19
    if n == 25:
        return 20
    if n == 26:
        return 21
    if n == 27:
        return 22
    if n == 28:
        return 23
    if n == 29:
        return 24
    if n == 30:
        return 24
    if n == 31:
        return 25
    if n == 32:
        return 26
    if n == 33:
        return 27
    if n == 34:
        return 28
    if n == 35:
        return 29
    if n == 36:
        return 29
    if n == 37:
        return 30
    if n == 38:
        return 31
    if n == 39:
        return 32
    if n == 40:
        return 33
    if n == 41:
        return 34
    if n

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] > 1:
        print(0)
        return
    ans = 1
    for i in range(1, n):
        ans *= a[i]
        if ans > 10**18:
            print(-1)
            return
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] <= ans + 1:
            ans += a[i]
    print(ans + 1)

=======
Suggestion 6

def f(n, a):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 3
    if n == 5:
        return 3
    if n == 6:
        return 4
    if n == 7:
        return 5
    if n == 8:
        return 6
    if n == 9:
        return 7
    if n == 10:
        return 8
    if n == 11:
        return 9
    if n == 12:
        return 10
    if n == 13:
        return 11
    if n == 14:
        return 12
    if n == 15:
        return 13
    if n == 16:
        return 14
    if n == 17:
        return 15
    if n == 18:
        return 16
    if n == 19:
        return 17
    if n == 20:
        return 18
    if n == 21:
        return 19
    if n == 22:
        return 20
    if n == 23:
        return 21
    if n == 24:
        return 22
    if n == 25:
        return 23
    if n == 26:
        return 24
    if n == 27:
        return 25
    if n == 28:
        return 26
    if n == 29:
        return 27
    if n == 30:
        return 28
    if n == 31:
        return 29
    if n == 32:
        return 30
    if n == 33:
        return 31
    if n == 34:
        return 32
    if n == 35:
        return 33
    if n == 36:
        return 34
    if n == 37:
        return 35
    if n == 38:
        return 36
    if n == 39:
        return 37
    if n == 40:
        return 38
    if n == 41:
        return 39
    if n

=======
Suggestion 7

def print_list(l):
    for i in l:
        print(i,end=' ')
    print()

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    book = 0
    for i in range(N):
        if a[i] <= book + 1:
            book += a[i]
        else:
            break
    print(book + 1)

=======
Suggestion 9

def main():
    # 读入数据
    N = int(input())
    a = list(map(int, input().split()))

    # 计算答案
    ans = 0
    for i in range(N):
        if a[i] - 1 == ans:
            ans += 1

    # 输出答案
    print(ans)
