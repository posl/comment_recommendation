def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. 首先，我们从A中计算出每个数字的出现次数。
    # 2. 然后，我们将这些出现次数的平方相加。
    # 3. 最后，我们从总和中减去N。
    # 4. 除以2，因为我们计算了所有的对两次。
    # 5. 请注意，我们必须使用64位整数来存储总和，因为它可能会超过32位整数的范围。
    cnt = {}
    for a in A:
        if a in cnt:
            cnt[a] += 1
        else:
            cnt[a] = 1
    #print(cnt)
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)
