def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    charge = 0
    for i in range(M):
        if i == 0:
            charge += AB[i][0]
        else:
            charge += AB[i][0] - AB[i-1][1]
        if charge >= N:
            charge = N
        charge -= AB[i][1] - AB[i][0]
        if charge <= 0:
            print("No")
            return
    charge += T - AB[-1][1]
    if charge <= N:
        print("Yes")
    else:
        print("No")
