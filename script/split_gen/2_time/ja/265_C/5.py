def main():
    H, W = map(int, input().split())
    G = []
    for i in range(H):
        G.append(list(input()))
    now = [0, 0]
    while True:
        if G[now[0]][now[1]] == "U":
            if now[0] == 0:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[0] -= 1
        elif G[now[0]][now[1]] == "D":
            if now[0] == H-1:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[0] += 1
        elif G[now[0]][now[1]] == "L":
            if now[1] == 0:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[1] -= 1
        elif G[now[0]][now[1]] == "R":
            if now[1] == W-1:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[1] += 1
        else:
            print(-1)
            break
