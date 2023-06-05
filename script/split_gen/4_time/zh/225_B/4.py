def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    # 各頂点の次数を数える
    degree = [0] * n
    for a, b in edges:
        degree[a-1] += 1
        degree[b-1] += 1
    # 次数が2以上の頂点があればNo
    if any(d >= 2 for d in degree):
        print("No")
    else:
        print("Yes")
