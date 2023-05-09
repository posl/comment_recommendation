def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = -10 ** 10
    for i in range(n):
        path = []
        j = i
        while True:
            path.append(j)
            j = p[j]
            if j == i:
                break
        score = 0
        for j in path:
            score += c[j]
        if score <= 0:
            continue
        score *= (k // len(path))
        k_ = k % len(path)
        score_ = 0
        for j in range(k_):
            score_ += c[path[j]]
        ans = max(ans, score + score_)
    for i in range(n):
        score = 0
        j = i
        for _ in range(k):
            j = p[j]
            score += c[j]
            if j == i:
                break
        ans = max(ans, score)
    print(ans)

if __name__ == '__main__':
    main()