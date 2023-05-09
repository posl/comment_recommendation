def solve(n, uvw):
    # 深さ優先探索で、各ノードの深さを求める
    depth = [-1] * n
    depth[0] = 0
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in uvw[i]:
            if depth[j] != -1:
                continue
            depth[j] = depth[i] + w
            stack.append(j)
    
    # 各ノードの深さの奇偶を出力する
    for i in range(n):
        print(depth[i] % 2)

if __name__ == '__main__':
    solve()