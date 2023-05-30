def main():
    L, Q = map(int, input().split())
    tree = [L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            tree.append(x)
            tree.append(L - x)
            tree.sort()
        else:
            for i in range(len(tree)):
                if tree[i] >= x:
                    print(tree[i])
                    break
main()
