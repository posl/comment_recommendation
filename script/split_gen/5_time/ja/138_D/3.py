def main():
    n, q = map(int, input().split())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    px = []
    for i in range(q):
        px.append(list(map(int, input().split())))
    counter = [0] * n
    for p, x in px:
        counter[p-1] += x
    counter2 = [0] * (n+1)
    for i in range(n-1):
        a, b = edges[i]
        counter2[a] += counter[b-1]
        counter2[b] += counter[a-1]
    counter2 = counter2[1:]
    counter = [counter[i] + counter2[i] for i in range(n)]
    print(*counter)
