Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    mod = [0] * 200
    for a in A:
        mod[a % 200] += 1
    ans = 0
    for m in mod:
        ans += m * (m - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [a % 200 for a in A]
    C = {}
    for b in B:
        if b in C:
            C[b] += 1
        else:
            C[b] = 1
    ans = 0
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(x) % 200 for x in input().split()]
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] == A[j]:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * 200
    cnt[0] = 1
    for i in range(n):
        a[i] %= 200
        ans += cnt[a[i]]
        cnt[a[i]] += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    cnt = [0] * mod
    for a in A:
        cnt[a % mod] += 1
    ans = 0
    for c in cnt:
        if c > 1:
            ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    mod = 200
    d = {}
    for i in range(N):
        if i == 0:
            d[A[i] % mod] = 1
        else:
            tmp = {}
            for key in d.keys():
                if (key + A[i]) % mod in tmp.keys():
                    tmp[(key + A[i]) % mod] += d[key]
                else:
                    tmp[(key + A[i]) % mod] = d[key]
            if A[i] % mod in tmp.keys():
                tmp[A[i] % mod] += 1
            else:
                tmp[A[i] % mod] = 1
            d = tmp
    for key in d.keys():
        ans += d[key] * (d[key] - 1) // 2
    print(ans)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    B = [a%200 for a in A]
    #print(B)
    C = {}
    for i in range(N):
        if B[i] in C:
            C[B[i]] += 1
        else:
            C[B[i]] = 1
    #print(C)
    ans = 0
    for c in C.values():
        ans += c*(c-1)//2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 余りを数える
    mod200 = [0 for _ in range(200)]
    for a in A:
        mod200[a % 200] += 1
    
    # 余りが同じものの組み合わせを数える
    ans = 0
    for m in mod200:
        ans += m * (m - 1) // 2
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 余りを格納するリスト
    remainder = [0] * 200
    # 余りを計算
    for i in range(N):
        remainder[A[i] % 200] += 1
    # 余りが2以上のものを計算
    count = 0
    for i in range(200):
        if remainder[i] >= 2:
            count += remainder[i] * (remainder[i] - 1) // 2
    print(count)

=======
Suggestion 10

def solve(n, a):
    # write your code here
    # return ans
    pass
