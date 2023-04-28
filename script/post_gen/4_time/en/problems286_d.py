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
        total += A[i] * B[i]
    if total < X:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
    if sum <= x:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    total = 0
    for i in range(n):
        total += a[i] * b[i]
    if total <= x:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    sum = 0
    for i in range(N):
        sum += A[i] * B[i]

    if sum >= X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    sum = 0
    for i in range(n):
        sum += a[i] * b[i]
        if sum > x * 100:
            print("No")
            return

    if sum < x * 100:
        print("No")
        return

    print("Yes")

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ans = "No"
    for i in range(n):
        if a[i] <= x and b[i] > 0:
            ans = "Yes"
            break
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    for i in range(N):
        if X >= AB[i][0] * AB[i][1]:
            X -= AB[i][0] * AB[i][1]
        else:
            X %= AB[i][0]
    if X == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    from sys import stdin
    readline = stdin.readline

    N, X = map(int, readline().split())
    AB = [tuple(map(int, readline().split())) for _ in range(N)]

    ans = 'No'
    for i in range(1, 2**N):
        total = 0
        for j in range(N):
            if i & (1 << j):
                total += AB[j][0] * AB[j][1]
        if total == X:
            ans = 'Yes'
            break

    print(ans)

=======
Suggestion 9

def can_pay(x, a, b):
    if x == 0:
        return True
    if x < 0 or len(a) == 0:
        return False
    for i in range(0, b[0] + 1):
        if can_pay(x - a[0] * i, a[1:], b[1:]):
            return True
    return False

=======
Suggestion 10

def findCombinationsUtil(arr, index, num, reducedNum, A, B, N):
    # Base condition
    if (reducedNum < 0):
        return 0

    # If combination is
    # found, print it
    if (reducedNum == 0):
        #print(arr[:index])
        #print(A)
        #print(B)
        for i in range(index):
            for j in range(N):
                if A[j] == arr[i]:
                    if B[j] > 0:
                        B[j] -= 1
                    else:
                        return 0
        return 1

    # Find the previous number
    # stored in arr[]. It helps
    # in maintaining increasing
    # order
    prev = 1 if (index == 0) else arr[index - 1]

    # note loop starts from
    # previous number i.e. at
    # array location index - 1
    for k in range(prev, num + 1):
        # next element of
        # array is k
        arr[index] = k

        # call recursively with
        # reduced number
        if findCombinationsUtil(arr, index + 1, num, reducedNum - k, A, B, N) == 1:
            return 1

    return 0
