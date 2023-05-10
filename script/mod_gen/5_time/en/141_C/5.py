def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    players = [k - q for _ in range(n)]
    for i in a:
        players[i-1] += 1
    for i in players:
        if i > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()