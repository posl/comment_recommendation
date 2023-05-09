def main():
    n, k, q = map(int, input().split())
    players = [k-q]*n
    for i in range(q):
        players[int(input())-1] += 1
    for i in range(n):
        if players[i] > 0:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()