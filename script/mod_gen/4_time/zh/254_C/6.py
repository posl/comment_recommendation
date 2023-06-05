def solve(N, K, A):
    # 一旦K是1，那么就可以直接判断是否是升序
    if K == 1:
        if sorted(A) == A:
            return "Yes"
        else:
            return "No"
    # 如果K不是1，那么就要判断是否是可以排序的
    # 首先要判断是否有重复的数字
    if len(set(A)) != N:
        return "Yes"
    # 如果没有重复的数字，那么就要判断是否可以排序
    # 首先要判断是否是连续的数字
    if sorted(A) == list(range(1, N+1)):
        return "Yes"
    # 如果不是连续的数字，那么就要判断是否可以排序
    # 首先要判断是否是连续的数字
    if sorted(A) == list(range(N, 0, -1)):
        return "Yes"
    # 如果不是连续的数字，那么就要判断是否可以排序
    # 首先要判断是否是连续的数字
    if sorted(A) == list(range(1, N+1))[::-1]:
        return "Yes"
    # 如果不是连续的数字，那么就要判断是否可以排序
    # 首先要判断是否是连续的数字
    if sorted(A) == list(range(N, 0, -1))[::-1]:
        return "Yes"
    # 如果不是连续的数字，那么就要判断是否可以排序
    # 首先要判断是否是连续的数字
    if sorted(A) == list(range(1, N+1)):
        return "Yes"
    # 如果不是连续的数字，那么就要判断是否可以排序
    # 首先要判断是否是连续的数字
    if sorted(A) == list(range(N, 0, -1)):
        return "Yes"
    # 如果不是连续的数字，那么就要判断是否可以排序
    # 首先

if __name__ == '__main__':
    solve()