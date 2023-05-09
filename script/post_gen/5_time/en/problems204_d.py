Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    t = list(map(int, input().split()))
    if n == 1:
        print(t[0])
    elif n == 2:
        print(max(t[0], t[1]))
    else:
        t.sort()
        print(max(t[0] + t[-2], t[1] + t[-1]))

=======
Suggestion 2

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    if N == 1:
        print(T[0])
    elif N == 2:
        print(max(T[0], T[1]))
    else:
        print(max(T[0], T[1]) + min(T[0], T[1]) + sum(T[2:]))

=======
Suggestion 3

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 <= oven2:
            oven1 += t.pop()
        else:
            oven2 += t.pop()
    print(max(oven1, oven2))

=======
Suggestion 4

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    t.reverse()
    oven1 = 0
    oven2 = 0
    for i in range(n):
        if oven1 <= oven2:
            oven1 += t[i]
        else:
            oven2 += t[i]
    print(max(oven1, oven2))

=======
Suggestion 5

def main():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    ans = t[-1]
    for i in range(n-2, -1, -1):
        ans = min(ans, t[i] + t[-1-i])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    T = list(map(int, input().split()))

    T.sort()
    T.reverse()

    oven1 = 0
    oven2 = 0

    for i in range(N):
        if oven1 <= oven2:
            oven1 += T[i]
        else:
            oven2 += T[i]

    print(max(oven1, oven2))

=======
Suggestion 7

def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    oven = [0, 0]
    for i in range(N):
        oven[0] += T[i]
        if oven[0] <= oven[1]:
            oven[1] = oven[0]
        else:
            oven[0] = oven[1]
    print(oven[1])

=======
Suggestion 8

def cooking_time(n, t):
    if n == 1:
        return t[0]
    elif n == 2:
        return max(t[0], t[1])
    else:
        oven1 = t[0]
        oven2 = t[1]
        for i in range(2, n):
            if oven1 <= oven2:
                oven1 += t[i]
            else:
                oven2 += t[i]
        return max(oven1, oven2)

=======
Suggestion 9

def main():
    n = int(input())
    t = [int(x) for x in input().split()]
    t.sort()
    print(t[-1])

=======
Suggestion 10

def main():
    # Get input
    num = int(input())
    times = list(map(int, input().split()))

    # Sort the list
    times.sort()

    # Initialize
    oven1 = 0
    oven2 = 0

    # Calculate the time
    for i in range(num):
        if oven1 <= oven2:
            oven1 += times[num-i-1]
        else:
            oven2 += times[num-i-1]

    # Print the result
    if oven1 <= oven2:
        print(oven2)
    else:
        print(oven1)
