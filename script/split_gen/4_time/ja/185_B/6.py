def solve():
    N,M,T = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(M)]
    if AB[0][0] != 1:
        print("No")
        exit()
    bat = N
    for i in range(M):
        bat -= AB[i][0] - (AB[i-1][1] if i > 0 else 0)
        if bat <= 0:
            print("No")
            exit()
        bat += AB[i][1] - AB[i][0]
        bat = min(bat,N)
    if bat - (T - AB[-1][1]) <= 0:
        print("No")
        exit()
    print("Yes")
    exit()
