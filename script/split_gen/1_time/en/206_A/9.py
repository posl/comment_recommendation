def main():
    N = int(input())
    tax = 1.08
    price = int(tax * N)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")
