Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    S = sum(A)
    count = [0] * (10**5 + 1)
    for a in A:
        count[a] += 1

    for i in range(Q):
        S += count[B[i]] * (C[i] - B[i])
        count[C[i]] += count[B[i]]
        count[B[i]] = 0
        print(S)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    sum_A = sum(A)
    count_B = [0] * (10 ** 5 + 1)
    for a in A:
        count_B[a] += 1

    for i in range(Q):
        b = B[i]
        c = C[i]
        sum_A += count_B[b] * (c - b)
        count_B[c] += count_B[b]
        count_B[b] = 0
        print(sum_A)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    sum_A = sum(A)
    count_B = [0] * 10**5
    for a in A:
        count_B[a-1] += 1

    for i in range(Q):
        sum_A += count_B[B[i]-1] * (C[i] - B[i])
        count_B[C[i]-1] += count_B[B[i]-1]
        count_B[B[i]-1] = 0
        print(sum_A)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    # カウントする
    count = [0] * (10**5+1)
    for a in A:
        count[a] += 1

    # 累積和をとる
    sum_count = [0] * (10**5+1)
    for i in range(len(count)):
        sum_count[i] = sum_count[i-1] + count[i]

    # 各クエリに対する処理
    for i in range(Q):
        # 値がB[i]の個数を求める
        num = sum_count[C[i]] - sum_count[B[i]-1]
        # C[i]に変換する
        count[B[i]] -= num
        count[C[i]] += num
        # 累積和を更新する
        for j in range(B[i], C[i]+1):
            sum_count[j] = sum_count[j-1] + count[j]

    # 答えを求める
    ans = 0
    for i in range(len(count)):
        ans += i * count[i]

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b,c = map(int,input().split())
        B.append(b)
        C.append(c)
    for i in range(Q):
        A = [C[i] if x == B[i] else x for x in A]
        print(sum(A))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    b = [0]*q
    c = [0]*q
    for i in range(q):
        b[i],c[i] = map(int,input().split())
    for i in range(q):
        for j in range(n):
            if a[j] == b[i]:
                a[j] = c[i]
    print(sum(a))

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = list()
    C = list()
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    sumA = sum(A)
    for i in range(Q):
        count = A.count(B[i])
        sumA -= B[i] * count
        sumA += C[i] * count
        print(sumA)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    cnt = [0] * (10**5 + 1)
    for a in A:
        cnt[a] += 1
    S = sum(A)
    for b, c in BC:
        S += (c - b) * cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(S)

=======
Suggestion 9

def main():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = map(int, input().split())
    Ac = Counter(A)
    ans = sum(A)
    for i in range(Q):
        ans += (C[i] - B[i])*Ac[B[i]]
        Ac[C[i]] += Ac[B[i]]
        Ac[B[i]] = 0
        print(ans)

=======
Suggestion 10

def read_int():
    return int(input())
