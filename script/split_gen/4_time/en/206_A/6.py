def main():
    N = int(input())
    tax = 1.08
    price = N * tax
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")
