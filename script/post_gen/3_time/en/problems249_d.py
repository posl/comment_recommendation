Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if A[i] == A[j]:
                continue
            if A[i] % A[j] == 0:
                ans += A.count(A[i] // A[j])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(i) for i in input().split()]

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (200001)
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(1, 200001):
        if B[i] == 0:
            continue
        for j in range(i, 200001, i):
            if j == i:
                ans += B[i] * (B[i] - 1) // 2
            else:
                ans += B[i] * B[j]
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if A[i] == A[j]:
                continue
            if A[i] == 1:
                ans += N - j - 1
                continue
            for k in range(j+1, N):
                if A[i] == A[k]:
                    continue
                if A[j] == A[k]:
                    continue
                if A[i] * A[j] == A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(raw_input())
a = map(int, raw_input().split())

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(N):
                if A[i] * A[j] == A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    Amax = max(A)
    cnt = [0] * (Amax + 1)
    for i in range(N):
        cnt[A[i]] += 1

    ans = 0
    for i in range(1, Amax + 1):
        if cnt[i] >= 2:
            ans += cnt[i] * (cnt[i] - 1) // 2
        for j in range(2 * i, Amax + 1, i):
            ans += cnt[i] * cnt[j]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A_iの約数を列挙する
    divisors = [[] for _ in range(2 * 10**5 + 1)]
    for i in range(1, 2 * 10**5 + 1):
        for j in range(i, 2 * 10**5 + 1, i):
            divisors[j].append(i)

    # A_iの約数のうち、A_jの約数の数を数える
    cnt = [0] * (2 * 10**5 + 1)
    for a in A:
        for d in divisors[a]:
            cnt[d] += 1

    # A_iの約数のうち、A_jの約数の数が2以上のものを列挙する
    # これらの数は、A_kの約数でもある
    # このとき、A_iの約数のうち、A_jの約数の数が2以上のものの個数を数える
    ans = 0
    for a in A:
        for d in divisors[a]:
            if cnt[d] >= 2:
                ans += 1
                break

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # A[i]で割り切れるものを数える
    # その中でA[i]より大きいものを数える
    # その中でA[i]より小さいものを数える
    # これらの積が答え
    # ただし、A[i]で割り切れるものが1つしかない場合は、その値を数えない
    # また、A[i]より大きいものが1つしかない場合は、その値を数えない
    # また、A[i]より小さいものが1つしかない場合は、その値を数えない
    
    # A[i]で割り切れるものを数える
    # これは、A[i]の約数を数えれば良い
    # ただし、A[i]の約数はA[i]の平方根までしか存在しない
    # なぜなら、A[i]の約数の組み合わせは、A[i]の平方根以下の約数とA[i]の平方根以上の約数の組み合わせで表現できるから
    # なので、A[i]の平方根までの約数を数えれば良い
    # ただし、A[i]の平方根が整数でない場合には、A[i]の平方根の切り捨てを数える
    # また、A[i]の平方根が1の場合には、A[i]の平方根を数える
    
    # A[i]の平方根を求める
    sqrt_A = [int(A[i] ** 0.5) for i in range(N)]
    
    # A[i]の平方根までの約

=======
Suggestion 10

def get_number_of_triplets(n, a):
    # write your code here
    return 0
