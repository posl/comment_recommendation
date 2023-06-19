Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    for i in range(2, n):
        ans += a[i // 2]
    print(ans)

=======
Suggestion 2

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
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += a[i]
    ans -= max(a)
    ans -= max(a)

    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    ans = sum(a)
    for i in range(n):
        ans -= min(a[i], a[i+1], a[i+2])
    print(ans)

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    tmp = 0
    for i in range(2*N-1):
        tmp += A[i]
        if i >= N:
            tmp -= A[i-N]
        if i >= N-1:
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i] + A[(i+1)%N]
    print(sum(B) - max(B))

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    ans = 0
    sum = 0
    for i in range(2*N):
        sum += A[i]
        if i >= N:
            sum -= A[i-N]
        if i >= N-1:
            ans = max(ans, sum)
    print(ans)

solve()

=======
Suggestion 8

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    # 从1开始，因为第一个人的舒适度为0
    B = [0] * (N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]

    # 原问题转换为：从第i个人开始，逆时针走，一直到第j个人结束，这个区间的最小值是多少
    # 用单调栈来解决
    # 从左往右扫描，栈里面存储的是递增的序列，如果遇到比栈顶小的数，就把栈顶弹出来，直到栈顶比当前数大，然后把当前数压入栈顶
    # 那么每个数进栈一次，出栈一次，所以算法复杂度是O(n)
    stack = []
    ans = 0
    for i in range(N+1):
        # 如果当前数比栈顶小，就把栈顶弹出来
        while len(stack) > 0 and A[stack[-1]] > A[i]:
            j = stack.pop()
            # 栈顶弹出来的时候，栈顶是第j个人，栈顶的下一个是第i个人
            # 那么，第j个人到第i个人之间的最小值是A[j]
            # 第j个人到第i个人之间的舒适度是A[j] * (B[i] - B[j])
            ans = max(ans, A[j] * (B[i] - B[j]))

        # 把当前数压入栈顶
        stack.append(i)

    print(ans)

solve()

=======
Suggestion 9

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 7
    A = [1, 1, 1, 1, 1, 1, 1]
    A = [2, 2, 1, 3]
    A = [1, 2, 3, 4, 5, 6, 7]
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    if N == 2:
        print(0)
        return

    A = A + A[0:2]
    A = A[2:N+2]
    A = A + A[0:2]
    A = A[2:N+2]
    A = A + A[0:2]
    A = A[2:N+2]
    A = A + A[0:2]
    A = A[2:N+2]
    A = A + A[0:2]

=======
Suggestion 10

def main():
    pass
