Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    for i in range(n):
        if a[i] == 1:
            b[i] = 1
            c[i] = 1
    for i in range(n):
        if b[i] == 1:
            for j in range(i + 1, n, i + 1):
                c[j] = 1 - c[j]
    ans = []
    for i in range(n):
        if c[i] == 1:
            ans.append(str(i + 1))
    print(len(ans))
    if len(ans) > 0:
        print(' '.join(ans))

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def solve(n, a):
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        s = sum(b[i::i]) % 2
        if s != a[i-1]:
            b[i] = 1
    return [i for i, x in enumerate(b) if x]

=======
Suggestion 4

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N, 0, -1):
        if sum([ans[j] for j in range(i, N, i)]) % 2 != a[i - 1]:
            ans.append(1)
        else:
            ans.append(0)
    M = sum(ans)
    print(M)
    if M > 0:
        print(*[i + 1 for i in range(N) if ans[i] == 1])
    return 0

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n)[::-1]:
        s = sum(b[i::i+1]) % 2
        if s != a[i]:
            b[i] = 1
    print(sum(b))
    print(*[i+1 for i, v in enumerate(b) if v])

=======
Suggestion 6

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N):
        if a[i] == 1:
            b[i] = 1
    print(sum(b))
    for i in range(N):
        if b[i] == 1:
            print(i + 1)

=======
Suggestion 7

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 0:
            print(0)
            return
        else:
            print(1)
            print(1)
            return
    if N == 2:
        if a[0] == 0 and a[1] == 0:
            print(0)
            return
        else:
            print(1)
            print(1)
            return
    if N == 3:
        if a[0] == 0 and a[1] == 0 and a[2] == 0:
            print(0)
            return
        else:
            print(1)
            print(1)
            return
    if N == 4:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            print(0)
            return
        else:
            print(1)
            print(1)
            return
    if N == 5:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0 and a[4] == 0:
            print(0)
            return
        else:
            print(1)
            print(1)
            return
    if N == 6:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0 and a[4] == 0 and a[5] == 0:
            print(0)
            return
        else:
            print(1)
            print(1)
            return
    if N == 7:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0 and a[4] == 0 and a[5] == 0 and a[6] == 0:
            print(0)
            return
        else:
            print(1)
            print(1)
            return
    if N == 8:
        if a[0] == 0 and a[1] == 0 and a

=======
Suggestion 8

def main():
    # 输入
    n = int(input())
    a = list(map(int, input().split()))

    # 算法
    def solve(n, a):
        # 1. 解决1的情况
        if a[0] == 1:
            if n == 1:
                return [1]
            else:
                return [-1]

        # 2. 解决n=2的情况
        if n == 2:
            if a[1] == 0:
                return [1]
            else:
                return [-1]

        # 3. 解决n>2的情况
        # 3.1 找出所有的3的倍数
        b = [i for i in range(2, n + 1) if i % 3 == 0]
        # 3.2 找出所有的3的倍数的和
        sum_b = sum(b)
        # 3.3 找出所有的3的倍数的和的模数
        mod_sum_b = sum_b % 2
        # 3.4 如果模数为0，就将2放到第一个盒子
        if mod_sum_b == 0:
            return [2] + b
        # 3.5 如果模数为1，就将1放到第一个盒子
        else:
            return [1] + b

    # 输出
    ans = solve(n, a)
    if ans == [-1]:
        print(-1)
    else:
        print(len(ans))
        print(*ans)

=======
Suggestion 9

def solve(n, a):
    if n == 1:
        if a[0] == 1:
            return [1]
        else:
            return []
    if n == 2:
        if a[0] == 0 and a[1] == 1:
            return [2]
        elif a[0] == 1 and a[1] == 0:
            return [1]
        else:
            return []
    if n == 3:
        if a[0] == 0 and a[1] == 0 and a[2] == 1:
            return [3]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0:
            return [2]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0:
            return [1]
        else:
            return []
    if n == 4:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 1:
            return [4]
        elif a[0] == 0 and a[1] == 0 and a[2] == 1 and a[3] == 0:
            return [3]
        elif a[0] == 0 and a[1] == 1 and a[2] == 0 and a[3] == 0:
            return [2]
        elif a[0] == 1 and a[1] == 0 and a[2] == 0 and a[3] == 0:
            return [1]
        else:
            return []
    if n == 5:
        if a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0 and a[4] == 1:
            return [5]
        elif a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 1 and a[4] == 0:
            return [4]
        elif a[0] == 0 and a[1] == 0 and a[2] == 1 and a[3] ==
