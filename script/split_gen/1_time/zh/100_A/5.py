def main():
    A,B = (int(x) for x in input().split())
    if A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")
