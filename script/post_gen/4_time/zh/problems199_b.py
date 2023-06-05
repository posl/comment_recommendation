Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_a = max(a)
    min_b = min(b)

    if max_a > min_b:
        print(0)
    else:
        print(min_b - max_a + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(max(0, min(B) - max(A) + 1))

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    min = max(a)
    max = min
    for i in range(n):
        if max < b[i]:
            max = b[i]
    print(max - min + 1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for x in range(1, 1001):
        ok = True
        for i in range(N):
            if x < A[i] or x > B[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)

=======
Suggestion 5

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    return n, a, b

=======
Suggestion 6

def solve(N, A, B):
    res = 0
    for x in range(1, 1001):
        for i in range(N):
            if x < A[i] or x > B[i]:
                break
        else:
            res += 1
    return res

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, A, B))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        for j in range(n):
            if i < a[j] or i > b[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    count = 0
    for i in range(1,1001):
        flag = True
        for j in range(n):
            if a[j] > i or b[j] < i:
                flag = False
                break
        if flag == True:
            count += 1
    print(count)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1001):
        flag = True
        for j in range(N):
            if i < A[j] or i > B[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
