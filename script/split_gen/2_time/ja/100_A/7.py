def main():
    A, B = map(int, input().split())
    if (A + B) <= 16 and (A + B) > 3 and A != 1 and B != 1:
        print("Yay!")
    else:
        print(":(")
