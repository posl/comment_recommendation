def main():
    input = int(input())
    price = int(input * 1.08)
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")
