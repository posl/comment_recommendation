def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    # 順列を作る
    def permutation(N, r):
        if r == 0:
            yield []
        else:
            for i in range(N):
                for p in permutation(N, r - 1):
                    if i not in p:
                        yield [i] + p
    # 町を訪れる経路は全部で N! 通りあります。
    # 1 番目に訪れる町から出発し、2 番目に訪れる町、3 番目に訪れる町、...、を経由し、N 番目に訪れる町に到着するまでの移動距離 (町から町への移動は直線移動とします) を、その経路の長さとします。
    # これらの N! 通りの経路の長さの平均値を計算してください。
    total = 0
    count = 0
    for p in permutation(N, N):
        # 経路の長さを計算
        for i in range(1, N):
            total += ((x[p[i - 1]] - x[p[i]]) ** 2 + (y[p[i - 1]] - y[p[i]]) ** 2) ** 0.5
        count += 1
    print(total / count)

if __name__ == '__main__':
    main()