def main():
    # 读取输入
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    # 二分查找
    ok = 10 ** 9
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if check(a, mid, k):
            ok = mid
        else:
            ng = mid
    print(ok)
