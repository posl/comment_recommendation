Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        s = sum(b[i::i]) % 2
        if s != a[i - 1]:
            b[i] = 1
    print(sum(b))
    print(*[i for i, v in enumerate(b) if v][1:])

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*n
    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i, n, i+1):
            sum += b[j]
        if sum%2 != a[i]:
            b[i] = 1
    print(sum(b))
    for i in range(n):
        if b[i] == 1:
            print(i+1, end=' ')
    print()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = [0] * n

    for i in range(n - 1, -1, -1):
        tmp = 0
        for j in range(i + 1, n, i + 1):
            tmp += b[j]
        if tmp % 2 != a[i]:
            b[i] = 1

    ans = []
    for i in range(n):
        if b[i] == 1:
            ans.append(i + 1)

    if len(ans) == 0:
        print(0)
    else:
        print(len(ans))
        print(*ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    for i in range(N-1, -1, -1):
        if sum(B[i::i+1])%2 != A[i]:
            B[i] = 1
    print(sum(B))
    print(*[i+1 for i, b in enumerate(B) if b], sep='\n')

=======
Suggestion 5

def main():
    N = int(input())
    a = list(map(int, input().split()))

    if sum(a) == 0:
        print(0)
        return

    if sum(a) % 2 == 1:
        print(-1)
        return

    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)

    print(len(ans))
    print(*ans)

=======
Suggestion 6

def check(a):
    n = len(a)
    for i in range(1,n+1):
        s = 0
        for j in range(1,n+1):
            if j%i == 0:
                s += a[j-1]
        if s%2 != a[i-1]:
            return False
    return True

n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n):
    if check(b + [0]) and check(b + [1]):
        b.append(0)
    else:
        b.append(1)
print(sum(b))
for i in range(n):
    if b[i] == 1:
        print(i+1)

=======
Suggestion 7

def main():
    # get input
    n = int(input())
    a = list(map(int, input().split()))

    # solve
    b = [0] * n
    for i in range(n-1, -1, -1):
        s = sum(b[i::i+1]) % 2
        if s != a[i]:
            b[i] = 1

    # output
    ans = [i+1 for i in range(n) if b[i] == 1]
    print(len(ans))
    if len(ans) > 0:
        print(*ans)

=======
Suggestion 8

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()]
    return n, a

=======
Suggestion 9

def main():
    # Get the input
    n = int(input())
    a = list(map(int, input().split()))

    # Initialize the output
    b = []

    # Check if there is a good set of choices
    for i in range(n-1, -1, -1):
        if a[i] == 1:
            b.append(i+1)
            for j in range(1, i//2+1):
                a[j] = 1 - a[j]
            if i == 0:
                break

    # Print the output
    if sum(a) == 0:
        print(len(b))
        for i in range(len(b)):
            print(b[i])
    else:
        print(-1)

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    #print(n)
    #print(a)

    # Check if a good set of choices exists
    # If a good set of choices exists, print one such set of choices
    # If a good set of choices does not exist, print -1

    # If there is no 1, then the answer is -1
    if 1 not in a:
        print(-1)
        return

    # If there is no 0, then the answer is 0
    if 0 not in a:
        print(0)
        return

    # If there is 1 and 0, then the answer is 1
    print(1)
    print(1)
    return
