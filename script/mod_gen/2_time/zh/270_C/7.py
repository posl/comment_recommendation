def main():
    n, x, y = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(n - 1)]
    print(uv)
    # ここにコードを追記
    # 1 から各頂点への最短距離を求める
    # 1 から x, y への最短距離を求める
    # x, y から各頂点への最短距離を求める
    # 1 から x までの最短距離 + 1 + y から各頂点への最短距離
    # 1 から y までの最短距離 + 1 + x から各頂点への最短距離
    # これらの最小値が答え

if __name__ == '__main__':
    main()