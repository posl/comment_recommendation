Synthesizing 10/10 solutions

=======
Suggestion 1

def problems173_d():
    return None

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(1, N):
        ans += A[i // 2]
    print(ans)

main()

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a += a
    s = [0] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        s[i] = s[i - 1] + a[i - 1]
    ans = 0
    for i in range(n):
        ans = max(ans, s[i + n] - s[i] + min(a[i:i + n]))
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    t = 0
    for i in range(2*N):
        t += A[i]
        if i >= N:
            t -= A[i-N]
        if i >= N-1:
            ans = max(ans, t)
    print(ans)

solve()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    a.append(a[2])
    a.append(a[3])
    a.append(a[4])
    a.append(a[5])
    a.append(a[6])
    a.append(a[7])
    a.append(a[8])
    a.append(a[9])
    a.append(a[10])
    a.append(a[11])
    a.append(a[12])
    a.append(a[13])
    a.append(a[14])
    a.append(a[15])
    a.append(a[16])
    a.append(a[17])
    a.append(a[18])
    a.append(a[19])
    a.append(a[20])
    a.append(a[21])
    a.append(a[22])
    a.append(a[23])
    a.append(a[24])
    a.append(a[25])
    a.append(a[26])
    a.append(a[27])
    a.append(a[28])
    a.append(a[29])
    a.append(a[30])
    a.append(a[31])
    a.append(a[32])
    a.append(a[33])
    a.append(a[34])
    a.append(a[35])
    a.append(a[36])
    a.append(a[37])
    a.append(a[38])
    a.append(a[39])
    a.append(a[40])
    a.append(a[41])
    a.append(a[42])
    a.append(a[43])
    a.append(a[44])
    a.append(a[45])
    a.append(a[46])
    a.append(a[47])
    a.append(a[48])
    a.append(a[49])
    a.append(a[50])
    a.append(a[51])
    a.append(a[52])
    a.append(a[53])
    a.append(a[54])
    a.append(a[55])
    a.append(a[56])
    a.append(a[57])
    a.append(a[58])
    a.append(a[59])
    a.append(a[60])
    a.append(a[61])
    a.append(a[62])
    a.append(a[63])
    a.append(a[64])
    a.append(a[65])
    a.append(a[66])
    a.append(a[67])
    a.append(a[

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.append(A[0])
    A.append(A[1])
    A.append(A[2])
    max = 0
    for i in range(1, N+1):
        sum = 0
        if i == 1:
            sum = A[i-1] + A[i+1]
            if sum > max:
                max = sum
        elif i == N:
            sum = A[i-1] + A[i+1]
            if sum > max:
                max = sum
        else:
            sum = A[i-1] + A[i+1]
            if sum > max:
                max = sum
    print(max)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])

    ans = 0
    for i in range(n):
        ans += max(a[i], a[i+1])

    print(ans)

=======
Suggestion 8

def solve():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    for i in range(1,n):
        ans += a[i]*i
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    cumsum = [0]
    for i in range(2 * N):
        cumsum.append(cumsum[-1] + A[i])
    ans = 0
    for i in range(N):
        ans = max(ans, cumsum[i + N] - cumsum[i + 1] + min(A[i], A[i + N]))
    print(ans)
