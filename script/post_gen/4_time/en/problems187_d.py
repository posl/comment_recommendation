Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    aoki = 0
    takahashi = 0
    for i in range(n):
        a, t = map(int, input().split())
        aoki += a
        takahashi += t
    if aoki > takahashi:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = A[::-1]
    B = B[::-1]
    count = 0
    for i in range(N):
        if (A[i] + count) % B[i] != 0:
            count += B[i] - (A[i] + count) % B[i]
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    aoki = sum(a)
    takahashi = 0
    for i in range(n):
        takahashi += a[i] + b[i]
    takahashi /= 2
    if aoki < takahashi:
        print(0)
    else:
        a.sort(reverse=True)
        b.sort(reverse=True)
        count = 0
        for i in range(n):
            aoki -= a[i]
            takahashi -= a[i] + b[i]
            count += 1
            if aoki < takahashi:
                break
        print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    max_a = max(A)
    max_a_index = A.index(max_a)
    max_b = max(B)
    max_b_index = B.index(max_b)
    if max_a_index == max_b_index:
        if max_a >= max_b:
            print(1)
        else:
            print(0)
    else:
        if max_a >= max_b:
            print(1)
        else:
            print(0)

=======
Suggestion 6

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    votes = []
    for i in range(N):
        votes.append(2*A[i] + B[i])
    #print(votes)
    votes.sort(reverse=True)
    #print(votes)
    total = sum(votes)
    #print(total)
    count = 0
    for i in range(N):
        count += 1
        total -= votes[i]
        if total < 0:
            break
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    max_b = max(b)
    idx = b.index(max_b)

    print(a[idx] + b[idx])

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(a)
    print(b)
    print(max(b) - min(a) + 1)

=======
Suggestion 9

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = 0
    takahashi = 0
    for i in range(N):
        if i % 2 == 0:
            aoki += AB[i][0]
        else:
            takahashi += AB[i][1]
    print(aoki - takahashi)

main()

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp = input().split(" ")
        a.append(int(tmp[0]))
        b.append(int(tmp[1]))
    t = 0
    for i in range(n):
        t += a[i]
    t = t/2
    c = 0
    for i in range(n):
        if t < b[i]:
            c += 1
    print(c)
