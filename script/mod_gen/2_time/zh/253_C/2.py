def solve():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    Q = int(input())
    S = []
    C = Counter()
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            S.append(x)
            C[x] += 1
        elif query[0] == '2':
            x, c = int(query[1]), int(query[2])
            for _ in range(min(c, C[x])):
                S.remove(x)
            C[x] -= min(c, C[x])
        else:
            print(max(S) - min(S))

if __name__ == '__main__':
    solve()