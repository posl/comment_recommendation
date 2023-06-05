def get_input():
    N, S = map(int, input().split())
    cards = []
    for i in range(N):
        cards.append(list(map(int, input().split())))
    return N, S, cards

if __name__ == '__main__':
    get_input()