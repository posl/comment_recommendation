Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    if N % 2 == 1:
        print(B[N // 2] - A[N // 2] + 1)
    else:
        print(B[N // 2] + B[N // 2 - 1] - A[N // 2] - A[N // 2 - 1] + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    Asum = [0]
    Bsum = [0]
    for i in range(N):
        Asum.append(Asum[i] + A[i])
        Bsum.append(Bsum[i] + B[i])
    ans = N
    for i in range(N):
        if A[i] > B[i]:
            ans = i
            break
    for i in range(N):
        if B[i] > A[N-1-i]:
            ans = min(ans, i)
            break
    for i in range(N):
        if A[i] > B[N-1-i]:
            ans = min(ans, i)
            break
    for i in range(N):
        if B[i] > A[N-1-i]:
            ans = min(ans, i)
            break
    for i in range(N):
        if A[i] > B[N-1-i]:
            ans = min(ans, i)
            break
    print(ans)

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
    C = []
    for i in range(N):
        C.append(A[i] + B[i])
    C.sort(reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        takahashi += A[i]
    for i in range(N):
        aoki += B[i]
    if takahashi > aoki:
        print(0)
    else:
        for i in range(N):
            if takahashi > aoki:
                print(i)
                break
            takahashi += C[i]
            aoki -= C[i]

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    A_sum = sum(A)
    B_sum = sum(B)
    if A_sum < B_sum:
        print(0)
        return
    else:
        ans = 0
        diff = A_sum - B_sum
        for i in range(N - 1, -1, -1):
            ans += 1
            diff += A[i] + B[i]
            if diff >= 0:
                print(ans)
                return

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
    A.sort()
    B.sort()
    if N%2 == 1:
        print(B[N//2] - A[N//2] + 1)
    else:
        print(B[N//2] + B[N//2-1] - A[N//2] - A[N//2-1] + 1)

=======
Suggestion 6

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        if i % 2 == 0:
            takahashi += AB[i][0]
        else:
            aoki += AB[i][1]
    if takahashi > aoki:
        print(0)
    else:
        for i in range(N):
            if i % 2 == 0:
                takahashi += AB[i][1] - AB[i][0]
            else:
                aoki += AB[i][0] - AB[i][1]
            if takahashi > aoki:
                print(i + 1)
                break

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    
    c = sorted(c, reverse=True)
    a = sorted(a, reverse=True)
    sum_a = sum(a)
    sum_c = 0
    for i in range(n):
        sum_c += c[i]
        if sum_c > sum_a:
            print(i + 1)
            break

main()

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    c.sort(reverse = True)
    ans = 0
    s = 0
    for i in range(n):
        s += c[i]
        ans += 1
        if s > sum(a):
            break
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, A, B)
    AB = [(a+b, a, b) for a, b in zip(A, B)]
    AB.sort(reverse=True)
    #print(AB)
    takahashi = 0
    aoki = 0
    for ab in AB:
        takahashi += ab[1]
        aoki += ab[2]
        if takahashi > aoki:
            print(AB.index(ab)+1)
            return
    print(N)

=======
Suggestion 10

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]

    ab.sort(key=lambda x: x[0] + x[1], reverse=True)
    aoki = sum([a for a, b in ab])
    takahashi = 0
    for i in range(n):
        takahashi += ab[i][0]
        aoki -= ab[i][0]
        if takahashi > aoki:
            print(i + 1)
            break
