def main():
    n = int(input())
    price = 206
    tax = 1.08
    if n < price/tax:
        print("Yay!")
    elif n == price/tax:
        print("so-so")
    else:
        print(":(")
