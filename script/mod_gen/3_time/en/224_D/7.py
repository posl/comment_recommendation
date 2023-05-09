def main():
    M = int(input())
    edge = []
    for i in range(M):
        u,v = map(int,input().split())
        edge.append((u,v))
    p = [0] + list(map(int,input().split()))
    for i in range(1,9):
        if p[i] == i:
            print(0)
            return
    for i in range(1,9):
        for j in range(1,9):
            if i == j:
                continue
            if p[i] == p[j]:
                print(-1)
                return
    for i in range(1,9):
        for j in range(1,9):
            if i == j:
                continue
            if p[i] == j:
                print(-1)
                return
    for i in range(1,9):
        for j in range(1,9):
            if i == j:
                continue
            if p[j] == i:
                print(-1)
                return
    for i in range(1,9):
        for j in range(1,9):
            if i == j:
                continue
            for k in range(1,9):
                if i == k or j == k:
                    continue
                if p[i] == p[j] == p[k]:
                    print(-1)
                    return
    for i in range(1,9):
        for j in range(1,9):
            if i == j:
                continue
            for k in range(1,9):
                if i == k or j == k:
                    continue
                if p[i] == p[j] == k:
                    print(-1)
                    return
    for i in range(1,9):
        for j in range(1,9):
            if i == j:
                continue
            for k in range(1,9):
                if i == k or j == k:
                    continue
                if p[i] == j == p[k]:
                    print(-1)
                    return
    for i in range(1,9):
        for j in range(1,9):
            if i == j:
                continue
            for k in range(1,9):
                if i == k or j == k:
                    continue
                if p[i] == j == k:
                    print(-1)
                    return
    for

if __name__ == '__main__':
    main()