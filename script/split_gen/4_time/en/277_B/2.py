def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    if len(set(cards)) == n:
        print("Yes")
    else:
        print("No")
