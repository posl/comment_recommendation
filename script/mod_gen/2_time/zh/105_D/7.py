def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 从左到右累积和
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    # 从左到右累积和的模
    t = [x % M for x in s]
    # 模的出现次数
    from collections import defaultdict
    d = defaultdict(int)
    for x in t:
        d[x] += 1
    # 从d中选出两个，计算排列数
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()