def main():
    n, q = map(int, input().split())
    # 1-indexed
    # 0: not following
    # 1: following
    following = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            following[a][b] = 1
        elif t == 2:
            following[a][b] = 0
        else:
            if following[a][b] == 1:
                print("Yes")
            else:
                print("No")
