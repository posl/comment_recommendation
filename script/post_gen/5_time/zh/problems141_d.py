Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(m):
        a.append(a.pop()//2)
    print(sum(a))
main()

=======
Suggestion 2

def solve(n, m, a):
    a.sort(reverse=True)
    for i in range(m):
        a[0] //= 2
        a.sort(reverse=True)
    return sum(a)

=======
Suggestion 3

def buyItemByDiscountTicket(itemPrice, ticketNum, ticketPrice):
    if ticketNum == 0:
        return itemPrice
    else:
        return buyItemByDiscountTicket(int(itemPrice/2), ticketNum-1, ticketPrice)

=======
Suggestion 4

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] //= 2
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for _ in range(M):
        A[-1] //= 2
        A.sort()
    print(sum(A))

=======
Suggestion 6

def get_min_price(N, M, A):
    A.sort()
    A.reverse()
    for i in range(M):
        A[0] = A[0] >> 1
        A.sort()
        A.reverse()
    return sum(A)

=======
Suggestion 7

def problem141_d():
    pass

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(m):
        a[-1] = a[-1] // 2
        a.sort()
    print(sum(a))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    print(sum(a))
