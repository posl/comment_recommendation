Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * 200
    for i in range(n):
        cnt[a[i] % 200] += 1
    ans = 0
    for i in range(200):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (A[i] - A[j]) % 200 == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 200
    for i in a:
        b[i % 200] += 1
    ans = 0
    for i in range(200):
        ans += b[i] * (b[i] - 1) // 2
    print(ans)

=======
Suggestion 4

def solve(N, A):
    cnt = [0] * 200
    for a in A:
        cnt[a % 200] += 1
    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2
    return ans

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] = A[i] % 200
    A.sort()
    ans = 0
    for i in range(N):
        j = i + 1
        while j < N and A[i] == A[j]:
            j += 1
        ans += (j - i) * (j - i - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [i % 200 for i in A]
    C = [B.count(i) for i in set(B)]
    ans = 0
    for i in C:
        ans += i * (i - 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [i % 200 for i in a]
    a.sort()
    ans = 0
    cnt = 1
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            cnt += 1
        else:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
    ans += cnt * (cnt - 1) // 2
    print(ans)

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    mod = [0] * 200
    for a in A:
        mod[a] += 1

    ans = 0
    for m in mod:
        if m > 1:
            ans += m * (m - 1) // 2

    print(ans)

=======
Suggestion 9

def problems200_c():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(A[0])
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
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #print(A[65])
    #print(A[66])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a%200 for a in A]
    A.sort()
    #print(A)
    cnt = 0
    i = 0
    while i < N-1:
        j = i+1
        while j < N:
            if A[i] == A[j]:
                cnt += 1
                j += 1
            else:
                i = j
                break
        if j == N:
            break
    print(cnt)
