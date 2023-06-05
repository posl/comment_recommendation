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
