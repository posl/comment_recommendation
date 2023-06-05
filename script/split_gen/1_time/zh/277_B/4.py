def main():
    n = int(input())
    cards = []
    for i in range(n):
        cards.append(input())
    if n == len(set(cards)):
        print("Yes")
    else:
        print("No")
