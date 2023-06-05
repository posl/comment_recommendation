def main():
    S = input()
    n = len(S)
    # 余数为key，出现次数为value
    mod = {i: 0 for i in range(2019)}
    mod[0] = 1
    # 从右往左，从1位数到n位数
    # 1位数
    x = 0
    for i in range(n):
        x += int(S[n-1-i]) * pow(10, i, 2019)
        x %= 2019
        mod[x] += 1
    # 2位数到n位数
    ans = 0
    for i in mod:
        # 从出现两次的余数中任选两个
        ans += mod[i] * (mod[i]-1) // 2
    print(ans)
