def main():
    # S_1 = input()
    # S_2 = input()
    # S_1 = "###"
    # S_2 = ".#."
    S_1 = ".#."
    S_2 = "##."
    if (S_1[0] == "#" or S_1[1] == "#") and (S_2[0] == "#" or S_2[1] == "#"):
        print("Yes")
    else:
        print("No")
