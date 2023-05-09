def main():
    M = int(input())
    edges = [list(map(int, input().split())) for _ in range(M)]
    pieces = list(map(int, input().split()))
    piece_pos = [0] * 9
    for i, p in enumerate(pieces):
        piece_pos[p] = i
    graph = [[] for _ in range(9)]
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    #print(graph)
    #print(piece_pos)
    #print(pieces)
    #print(edges)
    #print(pieces)
    #print(piece_pos)
    #print(graph)
    queue = []
    queue.append(pieces)
    visited = set()
    visited.add(tuple(pieces))
    ans = -1
    while queue:
        pieces = queue.pop(0)
        if pieces == [1,2,3,4,5,6,7,8]:
            ans = piece_pos[0]
            break
        for i in range(9):
            if pieces[i] == 0:
                empty_pos = i
                break
        for i in graph[empty_pos]:
            if piece_pos[i] != 0:
                tmp = pieces[:]
                tmp[i], tmp[empty_pos] = tmp[empty_pos], tmp[i]
                if tuple(tmp) not in visited:
                    visited.add(tuple(tmp))
                    queue.append(tmp)
    print(ans)

if __name__ == '__main__':
    main()