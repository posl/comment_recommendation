def main():
    N = int(input())
    S = input()
    for s in S:
        if s == "Z":
            print("A", end="")
        elif s == "Y":
            print("B", end="")
        elif s == "X":
            print("C", end="")
        elif s == "W":
            print("D", end="")
        elif s == "V":
            print("E", end="")
        elif s == "U":
            print("F", end="")
        elif s == "T":
            print("G", end="")
        elif s == "S":
            print("H", end="")
        elif s == "R":
            print("I", end="")
        elif s == "Q":
            print("J", end="")
        elif s == "P":
            print("K", end="")
        elif s == "O":
            print("L", end="")
        elif s == "N":
            print("M", end="")
        elif s == "M":
            print("N", end="")
        elif s == "L":
            print("O", end="")
        elif s == "K":
            print("P", end="")
        elif s == "J":
            print("Q", end="")
        elif s == "I":
            print("R", end="")
        elif s == "H":
            print("S", end="")
        elif s == "G":
            print("T", end="")
        elif s == "F":
            print("U", end="")
        elif s == "E":
            print("V", end="")
        elif s == "D":
            print("W", end="")
        elif s == "C":
            print("X", end="")
        elif s == "B":
            print("Y", end="")
        elif s == "A":
            print("Z", end="")
        else:
            print(chr(ord(s)+N), end="")
    print()
