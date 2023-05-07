def main():
    N, M, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.append([T, T])
    charge = N
    for i in range(M):
        charge -= AB[i][0] - AB[i-1][1]
        if charge <= 0:
            print("No")
            return
        charge += AB[i][1] - AB[i][0]
        charge = min(N, charge)
    print("Yes")

if __name__ == '__main__':
    main()