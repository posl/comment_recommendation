def main():
    n, q = map(int, input().split())
    p = [i for i in range(n+1)]
    head = [i for i in range(n+1)]
    tail = [i for i in range(n+1)]
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            p[head[query[2]]] = p[tail[query[1]]]
            p[tail[query[1]]] = query[2]
            tail[head[query[2]]] = tail[query[1]]
            head[query[2]] = head[query[1]]
            head[query[1]] = 0
            tail[query[1]] = 0
        elif query[0] == 2:
            p[tail[query[2]]] = p[tail[query[1]]]
            p[head[query[1]]] = query[2]
            tail[query[1]] = 0
            tail[query[2]] = tail[query[1]]
            head[query[1]] = 0
        else:
            print(' '.join(map(str, [i for i in range(1, n+1) if p[i] == p[query[1]]])))
