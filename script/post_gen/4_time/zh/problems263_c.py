Synthesizing 10/10 solutions

=======
Suggestion 1

def printAllList(n,m):
    if n == 1:
        for i in range(1,m+1):
            print(i)
    else:
        for i in range(1,m+1):
            print(i)
            printAllList(n-1,m)
            print(i)

=======
Suggestion 2

def print_sequence(n, m, seq):
    if len(seq) == n:
        print(' '.join(map(str, seq)))
    else:
        start = 1
        if len(seq) > 0:
            start = seq[-1] + 1
        for i in range(start, m + 1):
            seq.append(i)
            print_sequence(n, m, seq)
            seq.pop()

=======
Suggestion 3

def print_list(l):
    print(' '.join(map(str, l)))

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    a = [0]*n
    def dfs(i, x):
        if i == n:
            print(*a)
            return
        for j in range(x+1, m+1):
            a[i] = j
            dfs(i+1, j)
    dfs(0,0)

=======
Suggestion 5

def print_all_sequences(n,m):
    """
    打印所有长度为N的严格递增的整数序列，其中所有元素都在1到M之间（包括），按词典上的升序排列。
    :param n: 序列长度
    :param m: 序列元素最大值
    :return:
    """
    def print_sequence(seq):
        """
        打印序列
        :param seq:
        :return:
        """
        for i in range(len(seq)):
            print(seq[i],end=" ")
        print("")

    def print_all_sequences_helper(seq, i):
        """
        打印所有长度为N的严格递增的整数序列，其中所有元素都在1到M之间（包括），按词典上的升序排列。
        :param seq: 保存序列的数组
        :param i: 当前正在处理的元素的下标
        :return:
        """
        if i == n:
            print_sequence(seq)
            return
        # 从前一个元素的值加1开始，到m结束
        for j in range(1 if i == 0 else seq[i-1]+1,m+1):
            seq[i] = j
            print_all_sequences_helper(seq,i+1)

    seq = [0] * n
    print_all_sequences_helper(seq,0)

=======
Suggestion 6

def print_all_sequence(n, m):
    if n == 0:
        print()
    else:
        for i in range(1, m + 1):
            print(i, end=' ')
            print_all_sequence(n - 1, i - 1)
            print()

=======
Suggestion 7

def func(n, m):
    if n == 1:
        return [[i] for i in range(1, m+1)]
    else:
        return [i+[j] for i in func(n-1, m) for j in range(i[-1]+1, m+1)]

=======
Suggestion 8

def dfs(n,m,a):
    if len(a) == n:
        print(a)
        return
    s = 1
    if len(a) > 0:
        s = a[-1] + 1
    for i in range(s, m + 1):
        a.append(i)
        dfs(n, m, a)
        a.pop()

=======
Suggestion 9

def print_list(l):
    print(l[0], end='')
    for i in range(1, len(l)):
        print(' ', end='')
        print(l[i], end='')
    print('')

=======
Suggestion 10

def f(N,M):
    if N == 1:
        for i in range(1,M+1):
            print(i)
    else:
        for i in range(1,M+1):
            f(N-1,M-i)
            print(i)
f(3,5)
