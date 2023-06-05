def solve(n):
    # 1. 如果n=2^k，答案是k
    # 2. 否则，答案是k+1，其中k是n的二进制表示中的1的数量
    k = 0
    while n > 0:
        k += n % 2
        n //= 2
    return k
