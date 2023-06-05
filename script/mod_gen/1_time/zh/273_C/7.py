def solve():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))
    # 用于存储答案
    ans = [0] * N
    # 用于存储之前的出现过的数字
    used = set()
    # 用于存储之前的出现过的数字的个数
    used_count = 0
    # 从后往前遍历
    for i in range(N - 1, -1, -1):
        # 如果A[i]之前没有出现过
        if A[i] not in used:
            # 之前出现过的数字的个数+1
            used_count += 1
            # 将A[i]加入到已经出现过的数字中
            used.add(A[i])
        # 之前出现过的数字的个数就是答案
        ans[i] = used_count
    # 输出答案
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    solve()