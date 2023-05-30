def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    # 魔法の組み合わせを求める
    magic = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            magic.append((X[i] - X[j], Y[i] - Y[j]))
    # 魔法の組み合わせの中で最大の組み合わせが何回使われるかを求める
    ans = 0
    for a, b in magic:
        cnt = 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if (X[i] - X[j], Y[i] - Y[j]) == (a, b):
                    cnt += 1
        ans = max(ans, cnt)
    print(N - ans)
main()
