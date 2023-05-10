def main():
    N = int(input())
    cards = []
    for i in range(N):
        cards.append(input())
    for i in range(N):
        for j in range(i+1, N):
            if cards[i] == cards[j]:
                print("No")
                return
    print("Yes")
