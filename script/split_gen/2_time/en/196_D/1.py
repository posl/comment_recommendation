def main():
    H, W, A, B = map(int, input().split())
    def dfs(i, bit, A, B):
        if i == H * W:
            return 1
        if bit >> i & 1:
            return dfs(i + 1, bit, A, B)
        res = 0
        if B:
            res += dfs(i + 1, bit | 1 << i, A, B - 1)
        if A:
            if i % W != W - 1 and not bit & 1 << (i + 1):
                res += dfs(i + 1, bit | 1 << i | 1 << (i + 1), A - 1, B)
            if i + W < H * W:
                res += dfs(i + 1, bit | 1 << i | 1 << (i + W), A - 1, B)
        return res
    print(dfs(0, 0, A, B))
