Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0]
    for i in range(1, N):
        ans = (ans + A[i] - 1) // A[i] * A[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    ans = A[0]
    for i in range(1,N):
        ans = (ans+A[i]+1)//2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    ans = A[0] - 1
    for i in range(1, N):
        ans += A[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(n-1):
        if a[i] <= a[i+1]:
            ans += a[i+1] - a[i] + 1
            a[i+1] = a[i] - 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = A[-1] - 1
    for i in range(N-1):
        ans = min(ans, A[i])
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    h = 0
    for i in range(N-1):
        if A[i] <= h:
            break
        h = A[i] - h
    print(h)

=======
Suggestion 7

def solve(N, A):
    A = sorted(A, reverse=True)
    if N == 2:
        return A[0]
    if N == 3:
        return A[0] - A[1] + A[2]
    if N == 4:
        return A[0] - A[1] + A[2] - A[3]
    if N % 2 == 0:
        return A[0] - A[1] + A[2] - A[3] + A[4] - A[5] + A[6] - A[7] + A[8] - A[9] + A[10] - A[11] + A[12] - A[13] + A[14] - A[15] + A[16] - A[17] + A[18] - A[19] + A[20] - A[21] + A[22] - A[23] + A[24] - A[25] + A[26] - A[27] + A[28] - A[29] + A[30] - A[31] + A[32] - A[33] + A[34] - A[35] + A[36] - A[37] + A[38] - A[39] + A[40] - A[41] + A[42] - A[43] + A[44] - A[45] + A[46] - A[47] + A[48] - A[49] + A[50] - A[51] + A[52] - A[53] + A[54] - A[55] + A[56] - A[57] + A[58] - A[59] + A[60] - A[61] + A[62] - A[63] + A[64] - A[65] + A[66] - A[67] + A[68] - A[69] + A[70] - A[71] + A[72] - A[73] + A[74] - A[75] + A[76] - A[77] + A[78] - A[79] + A[80] - A[81] +

=======
Suggestion 8

def solve(n, a):
    a.sort(reverse=True)
    ans = 0
    for i in range(n-1):
        ans += a[i] - a[i+1]
    return ans + a[-1]
