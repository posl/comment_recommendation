Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n-1, -1, -1):
        if sum(a[i::i+1]) % 2 != a[i]:
            ans.append(i+1)
            a[i] = 1
    print(len(ans))
    print(*ans)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N-1, -1, -1):
        if a[i] == 0:
            continue
        ans.append(i+1)
        for j in range(2*i+1, N, i+1):
            a[j] = 1 - a[j]
    print(len(ans))
    print(*ans, sep=' ')

=======
Suggestion 3

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N - 1, -1, -1):
        if sum(b[i::i + 1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i + 1)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N-1, -1, -1):
        if sum(b[i::i+1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i+1, end=" ")

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1, -1, -1):
        if sum(B[i::i + 1]) % 2 != A[i]:
            B[i] = 1
    print(sum(B))
    print(*[i + 1 for i, x in enumerate(B) if x])

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(N):
        if a[N-i-1] == 1:
            b.append(N-i)
            for j in range(N-i-1, N, N-i-1):
                a[j] = 1 - a[j]
    print(len(b))
    print(' '.join(map(str, b)))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = 0
    B = []
    for i in range(N-1, -1, -1):
        if sum(A[i::i+1]) % 2 != A[i]:
            M += 1
            B.append(i+1)
    print(M)
    for b in B:
        print(b)

=======
Suggestion 8

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N, 0, -1):
        if sum(b[i - 1::i]) % 2 != a[i - 1]:
            b[i - 1] = 1
    print(sum(b))
    print(*[i + 1 for i in range(N) if b[i]])

=======
Suggestion 9

def main():
    N = int(input())
    a = list(map(int, input().split()))

    # 1つ目の要素について、2つ目以降の要素に対して、
    # 2つ目の要素の倍数であるかを判定する。
    # 2つ目の要素が2の倍数であれば、
    # 3つ目の要素が3の倍数であるか、4つ目の要素が4の倍数であるか、
    # 5つ目の要素が5の倍数であるか、というように、
    # 2つ目の要素の倍数であるかを判定する。
    # 2つ目の要素が2の倍数でなければ、
    # 3つ目の要素が3の倍数であるか、4つ目の要素が4の倍数であるか、
    # 5つ目の要素が5の倍数であるか、というように、
    # 2つ目の要素の倍数であるかを判定する。
    # これを、2つ目の要素がNの倍数であるか、
    # 3つ目の要素がNの倍数であるか、4つ目の要素がNの倍数であるか、
    # 5つ目の要素がNの倍数であるか、というように、
    # Nつ目の要素がNの倍数であるかを判定する。

    # 1つ目の要素について、2つ目以降の要素に対して、
    # 2つ目の要素の倍数であるかを判定する。
    # 2つ目の要素が2の倍数であれば、
    # 3つ目の要素が3の倍数であるか、4つ目の要素が4の倍数であるか、
    # 5つ目

=======
Suggestion 10

def read_int():
    return int(input())
