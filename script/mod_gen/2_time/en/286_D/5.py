def main():
    N, X = [int(x) for x in input().split()]
    coins = []
    for i in range(N):
        A, B = [int(x) for x in input().split()]
        coins.append([A, B])
    sum = 0
    for i in range(N):
        sum += coins[i][0] * coins[i][1]
    if sum >= X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()