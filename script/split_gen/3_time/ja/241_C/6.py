def main():
    N = int(input())
    S = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                continue
            for d in range(4):
                cnt = 1
                for k in range(1, 6):
                    ni = i + k * dx[d]
                    nj = j + k * dy[d]
                    if ni < 0 or ni >= N or nj < 0 or nj >= N:
                        break
                    if S[ni][nj] == "#":
                        cnt += 1
                    else:
                        break
                if cnt == 6:
                    print("Yes")
                    return
    print("No")
