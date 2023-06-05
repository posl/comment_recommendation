def main():
    # 读入数据
    N = int(input())
    A = [int(x) for x in input().split()]
    # 从后向前遍历
    ans = 0
    for i in range(N-1, -1, -1):
        # 判断是否满足条件
        if A[i] > ans:
            # 更新答案
            ans = A[i]
        else:
            # 凳子的高度为ans+1
            ans += 1
    
    # 打印答案
    print(ans)
