Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] == 0:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] % 2 == 0:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i == N-1 or A[i] != A[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [24, 11, 8, 3, 16]
    # N = 5
    # N = 10
    # A = [33, 18, 45, 28, 8, 19, 89, 86, 2, 4]
    # A = [5, 5, 5, 5]
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    A.sort()
    # print(A)
    # print(A)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    count = 0
    for i in range(1, n+1):
        if a[i] != a[i-1]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    for i in range(2,10**6+1):
        cnt_ = 0
        for j in range(N):
            if A[j] % i == 0:
                cnt_ += 1
        if cnt_ >= 2:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    m = A[-1] + 1
    p = [0] * m
    for i in range(N):
        while A[i] <= m:
            p[A[i]] += 1
            A[i] += A[i]
    ans = 0
    for i in range(N):
        if p[A[i]] == 1:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    pre = 0
    cnt = 0
    for i in range(N):
        if A[i] == pre:
            continue
        else:
            pre = A[i]
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 重複を取り除く
    a = list(set(a))
    a.sort()

    # 素数のリストを作る
    prime = [True] * (10**6 + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int((10**6 + 1)**0.5) + 1):
        if prime[i]:
            for j in range(i * 2, 10**6 + 1, i):
                prime[j] = False

    # 素因数分解
    def prime_factorize(n):
        arr = []
        temp = n
        for i in range(2, int(n**0.5) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])

        if temp != 1:
            arr.append([temp, 1])

        if arr == []:
            arr.append([n, 1])

        return arr

    # 素数のリストを作る
    prime = [True] * (10**6 + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, int((10**6 + 1)**0.5) + 1):
        if prime[i]:
            for j in range(i * 2, 10**6 + 1, i):
                prime[j] = False

    # 素因数分解
    def prime_factorize(n):
        arr = []
        temp = n
        for i in range(2, int(n**0.5) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])

        if temp != 1:
            arr.append([temp, 1])

        if arr == []:
            arr.append([n, 1])

        return arr

    # 素因数分解したも

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 最大値を求める
    maxA = max(A)

    # 素数リスト
    prime = []

    # 素数判定
    for i in range(2, maxA+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)

    # 素因数分解
    prime_factor = []
    for i in range(N):
        prime_factor.append([])
        for j in prime:
            if A[i] % j == 0:
                prime_factor[i].append(j)
                while A[i] % j == 0:
                    A[i] = A[i] // j

    # 素因数の種類を求める
    count = 0
    for i in prime_factor:
        if len(i) == 1:
            count += 1

    print(count)
