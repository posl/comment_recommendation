def main():
    N, W = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    d = [0] * 200001
    for s, t, p in data:
        d[s] += p
        d[t] -= p
    for i in range(1, 200001):
        d[i] += d[i-1]
    if max(d) <= W:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()