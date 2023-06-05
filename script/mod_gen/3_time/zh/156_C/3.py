def calcMinPower():
    N = int(input())
    X = list(map(int, input().split()))
    minPower = 1000000
    for P in range(1, 101):
        power = 0
        for i in range(N):
            power += (X[i] - P) ** 2
        if power < minPower:
            minPower = power
    print(minPower)
calcMinPower()
