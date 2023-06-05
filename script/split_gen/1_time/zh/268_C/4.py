def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [x - 1 for x in p]
    res = 0
    for i in range(N):
        if p[i] == i:
            res += 1
            if i < N - 1:
                p[i], p[i + 1] = p[i + 1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(res)
