def main():
    #input
    N = int(input())
    #calculation
    price = int(1.08 * N)
    #output
    if price < 206:
        print("Yay!")
    elif price == 206:
        print("so-so")
    else:
        print(":(")
