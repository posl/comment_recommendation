Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    count = 0
    while A < B:
        A *= K
        count += 1
    print(count)

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    count = 0
    while a < b:
        a *= k
        count += 1
    print(count)

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    counter = 0
    while A < B:
        A *= K
        counter += 1
    print(counter)

=======
Suggestion 4

def main():
    a,b,k = map(int, input().split())
    ans = 0
    while a < b:
        a *= k
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
    else:
        print(max(0, min(B - A - 1, K)))

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())

    if A >= B:
        print(0)
    elif B - A <= K:
        print(0)
    else:
        print(B - A - K)

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
        return
    if K == 1:
        print(B - A)
        return
    if K == 2:
        print(B - A)
        return
    if K == 3:
        print(B - A)
        return
    if K == 4:
        print(B - A)
        return
    if K == 5:
        print(B - A)
        return
    if K == 6:
        print(B - A)
        return
    if K == 7:
        print(B - A)
        return
    if K == 8:
        print(B - A)
        return
    if K == 9:
        print(B - A)
        return
    if K == 10:
        print(B - A)
        return
    if K == 11:
        print(B - A)
        return
    if K == 12:
        print(B - A)
        return
    if K == 13:
        print(B - A)
        return
    if K == 14:
        print(B - A)
        return
    if K == 15:
        print(B - A)
        return
    if K == 16:
        print(B - A)
        return
    if K == 17:
        print(B - A)
        return
    if K == 18:
        print(B - A)
        return
    if K == 19:
        print(B - A)
        return
    if K == 20:
        print(B - A)
        return
    if K == 21:
        print(B - A)
        return
    if K == 22:
        print(B - A)
        return
    if K == 23:
        print(B - A)
        return
    if K == 24:
        print(B - A)
        return
    if K == 25:
        print(B - A)
        return
    if K == 26:
        print(B - A)
        return
    if K == 27:
        print(B - A)
        return
    if K == 28:
        print(B - A)
        return
    if K == 29:
        print(B - A)
        return
    if K == 30

=======
Suggestion 8

def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
        return
    if K <= A:
        print(A - K)
        return
    if K <= A + B:
        print(0)
        return
    print(A - K + B)
