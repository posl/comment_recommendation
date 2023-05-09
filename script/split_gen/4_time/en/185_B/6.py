def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.append([T, T])
    if AB[0][0] != 0:
        AB.insert(0, [0, 0])
    charge = N
    for i in range(len(AB) - 1):
        charge -= AB[i + 1][0] - AB[i][1]
        if charge <= 0:
            print('No')
            return
        charge += AB[i + 1][1] - AB[i + 1][0]
        charge = min(charge, N)
    print('Yes')
