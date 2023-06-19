def get_input():
    n,s = map(int,input().split())
    cards = []
    for i in range(n):
        card = list(map(int,input().split()))
        cards.append(card)
    return n,s,cards

if __name__ == '__main__':
    get_input()