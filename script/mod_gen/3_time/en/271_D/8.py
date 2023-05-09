def f(n, s, cards):
    if n == 0:
        return s == 0
    if f(n - 1, s - cards[n - 1][0], cards):
        print('H', end='')
        return True
    if f(n - 1, s - cards[n - 1][1], cards):
        print('T', end='')
        return True
    return False
n, s = map(int, input().split())
cards = [list(map(int, input().split())) for i in range(n)]

if __name__ == '__main__':
    f()