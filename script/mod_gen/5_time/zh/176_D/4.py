def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    visited = [[float("inf") for _ in range(W)] for _ in range(H)]
    visited[C_h][C_w] = 0
    queue = [(C_h,C_w)]
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        h,w = queue.pop(0)
        if h == D_h and w == D_w:
            break
        for dh,dw in d:
            if 0 <= h+dh < H and 0 <= w+dw < W and S[h+dh][w+dw] == "." and visited[h+dh][w+dw] == float("inf"):
                visited[h+dh][w+dw] = visited[h][w]
                queue.append((h+dh,w+dw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                if 0 <= h+dh < H and 0 <= w+dw < W and S[h+dh][w+dw] == "." and visited[h+dh][w+dw] == float("inf"):
                    visited[h+dh][w+dw] = visited[h][w] + 1
                    queue.append((h+dh,w+dw))
    if visited[D_h][D_w] == float("inf"):
        print(-1)
    else:
        print(visited[D_h][D_w])

if __name__ == '__main__':
    main()