def check(a, b, c, edges):
    if (a, b) in edges and (b, c) in edges and (c, a) in edges:
        return True
    return False
N, M = map(int, input().split())
edges = []
for i in range(M):
    edges.append(tuple(map(int, input().split())))
count = 0
for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if check(a, b, c, edges):
                count += 1
print(count)

if __name__ == '__main__':
    check()