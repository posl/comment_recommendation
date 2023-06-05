Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = A + A
    sum = 0
    for i in range(N):
        sum += A[i]
    ans = 0
    for i in range(N):
        ans = max(ans, sum)
        sum -= A[i]
        sum += A[i+N]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    ans -= max(A)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 按照顺序到达的玩家的舒适度
    b = [0] * n
    # 反向到达的玩家的舒适度
    c = [0] * n

    # 累加和
    for i in range(n):
        b[(i + 1) % n] += a[i]
        c[(i - 1) % n] += a[i]

    # 最大值
    for i in range(1, n):
        b[i] = max(b[i - 1], b[i])
        c[n - i - 1] = max(c[n - i], c[n - i - 1])

    # 输出
    for i in range(n):
        print(max(b[i], c[i]))

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    A.insert(0,0)
    ans = 0
    for i in range(1,N):
        ans += A[i//2+1]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = sum(A)
    A_max = max(A)
    index = A.index(A_max)
    ans = A_sum - A_max
    if index == 0:
        ans += A_max
    else:
        ans += min(A[index - 1], A[index + 1])
    print(ans)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def solve(N, A):
    sum = 0
    for i in range(N-1):
        sum += A[i]
    max = 0
    for i in range(N):
        if A[i] > max:
            max = A[i]
    return sum - max

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    s = sum(a)
    m = 0
    for i in range(n):
        s -= a[i]
        m = max(m, a[i] + s)
    print(m)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 2:
        print(max(A))
        return

    # 1. find max A_i
    maxA = max(A)
    maxA_idx = A.index(maxA)

    # 2. find max A_i in the range [maxA_idx+1, N-1]
    maxA2 = max(A[maxA_idx+1:])

    # 3. find max A_i in the range [0, maxA_idx-1]
    maxA3 = max(A[:maxA_idx])

    print(maxA + max(maxA2, maxA3))

=======
Suggestion 10

def get_max_comfortable():
    player_num = int(input())
    player_list = list(map(int, input().split()))
    player_list.sort(reverse=True)
    total_comfortable = 0
    for i in range(player_num):
        if i == 0:
            total_comfortable += 0
        elif i == 1:
            total_comfortable += player_list[1]
        elif i == 2:
            total_comfortable += player_list[2]
        else:
            total_comfortable += player_list[i] + player_list[i-3]
    return total_comfortable
