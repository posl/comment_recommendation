def main():
    n = int(input())
    #print(n)
    tax = int(n * 1.08)
    #print(tax)
    if tax < 206:
        print("Yay!")
    elif tax == 206:
        print("so-so")
    else:
        print(":(")
