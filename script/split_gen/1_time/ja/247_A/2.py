def main():
    S = input()
    for i in range(len(S)):
        if i == len(S) - 1:
            print("0")
        elif S[i] == "1":
            print("1", end="")
        else:
            print("0", end="")
