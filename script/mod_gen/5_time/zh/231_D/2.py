def solve(n, m, a, b):
    # 从1开始，每个人的左右邻居
    neighbors = [set() for _ in range(n + 1)]
    for i in range(m):
        neighbors[a[i]].add(b[i])
        neighbors[b[i]].add(a[i])
    # 从1开始，每个人的左右邻居的左右邻居
    neighbors2 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors[i]:
            for k in neighbors[j]:
                if k != i:
                    neighbors2[i].add(k)
    # 从1开始，每个人的左右邻居的左右邻居的左右邻居
    neighbors3 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors2[i]:
            for k in neighbors[j]:
                if k != i and k not in neighbors[i]:
                    neighbors3[i].add(k)
    # 从1开始，每个人的左右邻居的左右邻居的左右邻居的左右邻居
    neighbors4 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors3[i]:
            for k in neighbors[j]:
                if k != i and k not in neighbors[i] and k not in neighbors2[i]:
                    neighbors4[i].add(k)
    # 从1开始，每个人的左右邻居的左右邻居的左右邻居的左右邻居的左右邻居
    neighbors5 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors4[i]:
            for k in neighbors[j]:
                if k != i and k not in neighbors[i] and k not in neighbors2[i] and k not in neighbors3[i]:
                    neighbors5[i].add(k)
    # 从1开始，每个人的左右邻居的

if __name__ == '__main__':
    solve()