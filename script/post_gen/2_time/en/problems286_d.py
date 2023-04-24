Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i]*B[i]
    if total <= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i] * B[i]
    if total >= X:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    sum = 0
    for i in range(N):
        sum += A[i] * B[i]
    if sum <= X:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    total = 0
    for i in range(N):
        total += A[i] * B[i]
    if total < X:
        print('No')
        return

    total = 0
    for i in range(N):
        total += A[i] * B[i]
        if total >= X:
            print('Yes')
            return

solve()

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        x -= a * b
    if x < 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    N, X = [int(x) for x in input().split()]
    coins = []
    for i in range(N):
        A, B = [int(x) for x in input().split()]
        coins.append([A, B])

    sum = 0
    for i in range(N):
        sum += coins[i][0] * coins[i][1]

    if sum >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve(n, x, a, b):
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
        if sum > x:
            return False
    if sum < x:
        return False
    return True

=======
Suggestion 8

def main():
    # Get input here
    n, x = map(int, input().strip().split())
    a = []
    b = []
    for _ in range(n):
        a1, b1 = map(int, input().strip().split())
        a.append(a1)
        b.append(b1)
    # Calculate result here
    result = solve(n, x, a, b)
    # Print output here
    print("Yes" if result else "No")

=======
Suggestion 9

def can_pay_exact(x, coins):
    if x == 0:
        return True
    if len(coins) == 0:
        return False
    if x < 0:
        return False
    if x >= coins[0]:
        return can_pay_exact(x - coins[0], coins[1:]) or can_pay_exact(x, coins[1:])
    else:
        return can_pay_exact(x, coins[1:])
    
n, x = map(int, input().split())

coins = []
for i in range(n):
    a, b = map(int, input().split())
    coins.append(a * b)

=======
Suggestion 10

def check_if_possible(N,X,A,B):
    coins = []
    for i in range(N):
        for j in range(B[i]):
            coins.append(A[i])
    coins.sort()
    coins.reverse()
    sum = 0
    for i in range(len(coins)):
        sum += coins[i]
        if sum >= X:
            return "Yes"
    return "No"
