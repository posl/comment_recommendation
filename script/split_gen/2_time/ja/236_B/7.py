def main():
    N = int(input())
    card = list(map(int, input().split()))
    card.sort()
    for i in range(4*N-1):
        if card[i] != card[i+1]:
            print(card[i])
            break
        else:
            i += 1
