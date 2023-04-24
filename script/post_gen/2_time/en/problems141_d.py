Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] // (2 ** M)
        A[i] %= (2 ** M)
        A.sort(reverse=True)
        for j in range(M):
            if A[j] == 0:
                break
            ans += 1
            A[j] -= 1
            A.sort(reverse=True)
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i]
        if i < m:
            ans = ans // 2
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if M == 0:
            break
        if A[i] >= 2**M:
            break
        else:
            A[i] = A[i]//(2**(bin(A[i]).count("1")-1))
            M -= bin(A[i]).count("1")
    if M > 0:
        A[i] = A[i]//(2**M)
    print(sum(A))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        y = 0
        x = A[i]
        while x % 2 == 0:
            x //= 2
            y += 1
        if y <= M:
            M -= y
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 5

def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] // (2**M)
        A[i] %= 2**M
        A.sort(reverse=True)
        for j in range(M):
            if A[i] == 0:
                break
            A[i] //= 2
            A.sort(reverse=True)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        print(A[i])
        for j in range(M):
            if A[i] >= A[i+1]:
                A[i] = A[i]/(2**(j+1))
            else:
                A[i] = A[i]/(2**(j))
    print(A)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    B = [0] * (M+1)
    for a in A:
        for i in range(M+1):
            if B[i] >= a:
                break
            if a > B[i] * 2:
                B[i+1] = max(B[i+1], B[i] * 2)
            else:
                B[i+1] = max(B[i+1], a)

    print(sum(B))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A = [0] + A
    #print(A)
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    #print(A)
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # 1. A を昇順にソートする
    # 2. A[i] が A[i-1] に対して 2^k 倍であるとして、
    #    A[i-1] を 2^k 倍したものを A[i] に置き換える
    # 3. A を降順にソートする
    # 4. A[i] に対して、M 個のチケットを使う
    # 5. A[i] を A[i-1] に置き換える
    # 6. A を降順にソートする
    # 7. 3 ～ 6 を A[0] に対して繰り返す
    # 8. A の総和を出力する

    for i in range(1, N):
        if A[i] % A[i-1] == 0:
            k = 0
            while A[i] % (2**k) == 0:
                k += 1
            A[i] = A[i-1] * (2**(k-1))

    for i in range(M):
        A[0] = A[0] // 2

    print(sum(A))

=======
Suggestion 10

def get_min_cost(n, m, a):
    a.sort(reverse=True)
    cost = 0
    for i in range(n):
        cost += a[i]
        if i < m:
            cost -= a[i] // 2
    return cost
