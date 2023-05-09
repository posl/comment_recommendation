def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    dist = [[float('inf')] * w for _ in range(h)]
    dist[ch][cw] = 0
    que = [(ch, cw)]
    while que:
        nh, nw = que.pop(0)
        if nh == dh and nw == dw:
            break
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh += dh
            nw += dw
            if nh < 0 or nh >= h or nw < 0 or nw >= w or s[nh][nw] == '#' or dist[nh][nw] != float('inf'):
                nh -= dh
                nw -= dw
                continue
            dist[nh][nw] = dist[nh-dh][nw-dw] + 1
            que.append((nh, nw))
            nh -= dh
            nw -= dw
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = dh + nh
                nw = dw + nw
                if nh < 0 or nh >= h or nw < 0 or nw >= w or s[nh][nw] == '#' or dist[nh][nw] != float('inf'):
                    nh -= dh
                    nw -= dw
                    continue
                dist[nh][nw] = dist[nh-dh][nw-dw] + 1
                que.append((nh, nw))
                nh -= dh
                nw -= dw
    if dist[dh][dw] == float('inf'):
        print(-1)
    else:
        print(dist[dh][dw])
main()
I got AC, but I think it's not the best solution.
I think the best solution is to use BFS, but I don't know how to implement it.
I think BFS is better than Dijkstra algorithm, because it's unnecessary to calculate the distance between each vertex.
I'm wondering how to implement BFS.
Thank you for reading my question.

if __name__ == '__main__':
    main()