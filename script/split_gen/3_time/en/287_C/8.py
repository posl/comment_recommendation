def main():
    n, m = map(int, input().split())
    if m != n-1:
        print("No")
        return
    nodes = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        nodes[u-1] += 1
        nodes[v-1] += 1
    if max(nodes) == 2:
        print("Yes")
    else:
        print("No")
