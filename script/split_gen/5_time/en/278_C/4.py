def main():
    n, q = map(int, input().split())
    follow = [[] for _ in range(n)]
    for _ in range(q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a].append(b)
        elif t == 2:
            if b in follow[a]:
                follow[a].remove(b)
        else:
            if b in follow[a] and a in follow[b]:
                print('Yes')
            else:
                print('No')
