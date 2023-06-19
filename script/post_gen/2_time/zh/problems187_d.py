Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum < b_sum:
        print(0)
        return
    else:
        diff = a_sum - b_sum
        count = 0
        for i in range(n-1,-1,-1):
            diff -= (a[i] - b[i])
            count += 1
            if diff < 0:
                break
        print(count)
        return

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a = sorted(a)
    b = sorted(b)
    max_a = a[-1]
    max_b = b[-1]
    if max_a >= max_b:
        print(1)
    else:
        print(0)

=======
Suggestion 3

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for i in range(n)]
    ab.sort(key=lambda x: 2*x[0]+x[1], reverse=True)
    #print(ab)
    x = 0
    for i in range(n):
        x += ab[i][0]
        if x > sum([ab[j][1] for j in range(i+1)]):
            print(i+1)
            break
    else:
        print(n)

=======
Suggestion 4

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N-1, -1, -1):
        A[i] += ans
        if A[i] % B[i] != 0:
            ans += B[i] - A[i] % B[i]
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N-1,-1,-1):
        A[i] += ans
        if A[i]%B[i] == 0:
            continue
        else:
            ans += B[i] - A[i]%B[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a.append(int(input().split()[0]))
        b.append(int(input().split()[1]))
    a_sum = sum(a)
    b_sum = sum(b)
    if a_sum > b_sum:
        print(0)
    else:
        a_b = [i for i in range(n)]
        for i in range(n):
            a_b[i] = a[i] - b[i]
        a_b.sort()
        a_b.reverse()
        a_b_sum = 0
        for i in range(n):
            a_b_sum += a_b[i]
            if a_b_sum + a_sum > b_sum:
                print(i+1)
                break

=======
Suggestion 7

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N-1, -1, -1):
        A[i] += ans
        if A[i] % B[i] != 0:
            ans += B[i] - A[i] % B[i]
    print(ans)

solve()

=======
Suggestion 8

def solve():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = 0
    for i in range(n):
        ans += a[i] * i + b[i] * (n - i)
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    j = 0
    cnt = 0
    while i < N and j < N:
        if A[i] > B[j]:
            cnt += 1
            i += 1
        else:
            i += 1
            j += 1
    print(cnt)

=======
Suggestion 10

def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i]
        ans -= B[i]
        if ans < 0:
            print(i+1)
            return
    print(N)
    return
