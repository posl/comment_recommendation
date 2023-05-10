Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[i] = a[i] // 2
    a.sort(reverse=True)
    print(sum(a[m:]))

=======
Suggestion 2

def calc(money, discnt):
    for i in range(discnt):
        money = money // 2
    return money

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    for i in range(m):
        a[-1] //= 2
        a.sort()

    print(sum(a))

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[i] //= 2
    A.sort(reverse=True)
    print(sum(A))

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A.append(0)
    i = 0
    while i < N and M > 0:
        if A[i] > A[i+1]:
            A[i] //= 2
            M -= 1
        else:
            i += 1
    print(sum(A))

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[0] = A[0]//2
        A.sort(reverse=True)
    print(sum(A))
    return 0

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    for i in range(m):
        a[i] = a[i]//2
    a.sort()
    a.reverse()
    print(sum(a))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # 割引券を使わない場合を初期値とする
    ans = sum(a)

    # 割引券を使う場合を考える
    # 割引券を使う場合は、割引券を使う品物の中で最も安いものを割引券で買うのが最適
    # 割引券を使う品物を全て試す
    for i in range(m):
        a.sort()
        a[0] = a[0] // 2

    print(sum(a))

=======
Suggestion 10

def calc_price(price, discount_ticket):
    if discount_ticket == 0:
        return price
    else:
        return int(price / (2 ** discount_ticket))
