def main():
    n = int(input())
    player = list(map(int, input().split()))
    player.sort()
    print(player[1])

if __name__ == '__main__':
    main()