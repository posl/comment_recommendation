def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    # 1. 1 から N までの各頂点について、その頂点から到達可能な頂点のうち、最大の H の値を求める
    # 2. 1 から N までの各頂点について、その頂点の H の値が、その頂点から到達可能な頂点のうち、最大の H の値以下であるとき、その頂点は良い頂点である
    # 1. 1 から N までの各頂点について、その頂点から到達可能な頂点のうち、最大の H の値を求める
    max_h = [0] * N
    for a, b in AB:
        max_h[a - 1] = max(max_h[a - 1], H[b - 1])
        max_h[b - 1] = max(max_h[b - 1], H[a - 1])
    # 2. 1 から N までの各頂点について、その頂点の H の値が、その頂点から到達可能な頂点のうち、最大の H の値以下であるとき、その頂点は良い頂点である
    ans = 0
    for i in range(N):
        if H[i] <= max_h[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()