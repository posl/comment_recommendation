def main():
    N = int(input())
    X = list(map(int, input().split()))
    min_power = 100000000
    for i in range(101):
        power = 0
        for j in range(N):
            power += (X[j]-i)**2
        if power < min_power:
            min_power = power
    print(min_power)

if __name__ == '__main__':
    main()