def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    count = 0
    for i in range(M):
        a = edges[i][0]
        b = edges[i][1]
        for j in range(i + 1, M):
            c = edges[j][0]
            d = edges[j][1]
            if b == c:
                if [a, d] in edges:
                    count += 1
            elif b == d:
                if [a, c] in edges:
                    count += 1
            elif a == c:
                if [b, d] in edges:
                    count += 1
            elif a == d:
                if [b, c] in edges:
                    count += 1
    print(count)
