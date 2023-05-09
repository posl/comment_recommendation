def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    if AB.count([i + 1, j + 1]) == AB.count([k + 1, l + 1]) and CD.count([i + 1, j + 1]) == CD.count([k + 1, l + 1]):
                        continue
                    else:
                        print("No")
                        return
    print("Yes")
    return
