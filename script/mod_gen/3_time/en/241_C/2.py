def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        for j in range(N):
            if S[i][j] == ".":
                S[i] = S[i][:j] + "#" + S[i][j+1:]
                for k in range(N):
                    for l in range(N):
                        if S[k][l] == ".":
                            S[k] = S[k][:l] + "#" + S[k][l+1:]
                            for m in range(N):
                                for n in range(N):
                                    if S[m][n] == ".":
                                        S[m] = S[m][:n] + "#" + S[m][n+1:]
                                        for o in range(N):
                                            for p in range(N):
                                                if S[o][p] == ".":
                                                    S[o] = S[o][:p] + "#" + S[o][p+1:]
                                                    for q in range(N):
                                                        for r in range(N):
                                                            if S[q][r] == ".":
                                                                S[q] = S[q][:r] + "#" + S[q][r+1:]
                                                                for s in range(N):
                                                                    for t in range(N):
                                                                        if S[s][t] == ".":
                                                                            S[s] = S[s][:t] + "#" + S[s][t+1:]
                                                                            for u in range(N):
                                                                                for v in range(N):
                                                                                    if S[u][v] == ".":
                                                                                        S[u] = S[u][:v] + "#" + S[u][v+1:]
                                                                                        for w in range(N):
                                                                                            for x in range(N):
                                                                                                if S[w][x] == ".":
                                                                                                    S[w] = S[w][:x] + "#" + S[w][x+1:]
                                                                                                    for y in range(N):
                                                                                                        for z in range(N):
                                                                                                            if S[y][z] == ".":
                                                                                                                S[y] = S[y][:z] + "#" + S[y][z+1:]
                                                                                                                for aa in range(N):
                                                                                                                    for bb in range(N):
                                                                                                                        if S[aa][bb] == ".":
                                                                                                                            S[aa] = S[aa][:bb] + "#" + S[aa][bb+1:]
                                                                                                                            for cc in range(N):
                                                                                                                                for dd in range(N):
                                                                                                                                    if S[cc][dd] == "."

if __name__ == '__main__':
    main()