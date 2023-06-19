Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:
                cnt += 1
        if cnt <= n - cnt and ans + (1 << i) <= k:
            ans += (1 << i)
    s = 0
    for i in range(n):
        s += ans ^ a[i]
    print(s)

=======
Suggestion 2

def main():
    # 读入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 处理
    # 1. 计算a中最大的值
    max_a = max(a)
    # 2. 计算max_a的位数
    max_a_len = len(bin(max_a)) - 2
    # 3. 如果k的位数小于max_a的位数，则k的位数扩展到max_a的位数
    if len(bin(k)) - 2 < max_a_len:
        k = k | (2 ** max_a_len - 1)
    # 4. 计算k的二进制表示
    k_bin = bin(k)[2:]
    # 5. 计算a中每个数的二进制表示
    a_bin = [bin(ai)[2:] for ai in a]
    # 6. 计算f(x)
    f = 0
    for i in range(max_a_len):
        # 6.1 计算a中每个数的第i位的1的个数
        one_num = 0
        for a_bin_i in a_bin:
            if len(a_bin_i) >= max_a_len - i and a_bin_i[max_a_len - i - 1] == '1':
                one_num += 1
        # 6.2 计算k的第i位的1的个数
        if len(k_bin) >= max_a_len - i and k_bin[max_a_len - i - 1] == '1':
            k_one_num = one_num
        else:
            k_one_num = n - one_num
        # 6.3 计算f(x)
        if k_one_num >= one_num:
            f += (2 ** (max_a_len - i - 1)) * one_num
        else:
            f += (2 ** (max_a_len - i - 1)) * (n - one_num)
    # 输出
    print(f)

=======
Suggestion 3

def f(x):
    sum = 0
    for a in A:
        sum += (x^a)
    return sum

N, K = map(int, input().split())
A = list(map(int, input().split()))
max = 0
for i in range(K+1):
    if f(i) > max:
        max = f(i)
print(max)

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        cnt = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                cnt += 1
        if cnt <= n//2:
            if ans + (1 << i) <= k:
                ans += 1 << i
    s = 0
    for i in range(n):
        s += ans ^ a[i]
    print(s)

=======
Suggestion 5

def xor(a,b):
    #a,b是字符串
    if a == '0' and b == '0':
        return '0'
    elif a == '1' and b == '1':
        return '0'
    else:
        return '1'

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    res = 0
    for i in range(40,-1,-1):
        s = 0
        for j in range(n):
            if (a[j] >> i) & 1:
                s += 1
        if s <= n//2 and res + (1 << i) <= k:
            res += (1 << i)
    print(sum(a)^res)

=======
Suggestion 7

def main():
    # 输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 计算a中所有元素的最大位数
    max_bit = len(bin(max(a))) - 2

    # 计算a中所有元素的二进制表示
    a_bin = [[0] * n for _ in range(max_bit)]
    for i in range(n):
        for j in range(max_bit):
            a_bin[j][i] = (a[i] >> j) & 1

    # 计算a中所有元素的二进制表示的前缀和
    a_bin_cum = [[0] * (n + 1) for _ in range(max_bit)]
    for i in range(max_bit):
        for j in range(n):
            a_bin_cum[i][j + 1] = a_bin_cum[i][j] + a_bin[i][j]

    # 计算a中所有元素的二进制表示的前缀和的最大值
    a_bin_cum_max = [0] * max_bit
    for i in range(max_bit):
        a_bin_cum_max[i] = max(a_bin_cum[i])

    # 计算a中所有元素的二进制表示的前缀和的最大值的二进制表示
    a_bin_cum_max_bin = [0] * max_bit
    for i in range(max_bit):
        a_bin_cum_max_bin[i] = (a_bin_cum_max[i] >> i) & 1

    # 计算a中所有元素的二进制表示的前缀和的最大值的二进制表示的前缀和
    a_bin_cum_max_bin_cum = [0] * (max_bit + 1)
    for i in range(max_bit):
        a_bin_cum_max_bin_cum[i + 1] = a_bin_cum_max_bin_cum[i] + a_bin_cum_max_bin[i]

    # 计算a中所有元素的二进制表示的前缀和的最大值的二进制表示的前缀和的最大值
    a_bin_cum_max_bin_cum_max = max(a_bin_cum_max_bin_cum)

    # 计算a中所有元素

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = map(int, input().split())
    A = list(A)
    A.sort()
    ans = 0
    for i in range(40, -1, -1):
        count = 0
        for j in range(N):
            if (A[j] >> i) & 1:
                count += 1
        if count <= N//2:
            if ans + (1 << i) <= K:
                ans += (1 << i)
    sum = 0
    for i in range(N):
        sum += ans ^ A[i]
    print(sum)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #N, K = 3, 7
    #A = [1, 6, 3]
    #N, K = 4, 9
    #A = [7, 4, 0, 3]
    #N, K = 1, 0
    #A = [1000000000000]
    #print(N, K, A)

    # 1. 先计算出每个数的二进制表示中有多少个1
    # 2. 从最高位开始，如果某个数的二进制表示中的某一位为1，则该位的值为1的数的个数为N-1个
    # 3. 如果某个数的二进制表示中的某一位为0，则该位的值为1的数的个数为N个
    # 4. 如果该位的值为1的数的个数大于该位的值为0的数的个数，则该位的值为1，否则为0
    # 5. 重复2-4步骤，直到计算出所有位的值
    # 6. 将所有位的值组合起来，得到最终的结果
    # 7. 如果K的二进制表示中的某一位为1，则最终结果的该位为0，否则为1
    # 8. 将最终结果转换为十进制，得到最终的结果
    # 9. 如果最终结果大于K，则最终结果为K
    # 10. 输出最终结果
    #print(bin(3), bin(5), bin(6))
    #print(bin(3^5), bin(3^6), bin(5^6))
    #print(bin(3^5^6))
    #print(bin(3^5^6).count('1'))
    #print(bin(3^5^6).count('0'))
    #print(bin(

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(41, -1, -1):
        cnt = 0
        for j in range(n):
            if a[j] >> i & 1:
                cnt += 1
        if cnt <= n - cnt and ans + (1 << i) <= k:
            ans += 1 << i
    s = 0
    for i in range(n):
        s += ans ^ a[i]
    print(s)
