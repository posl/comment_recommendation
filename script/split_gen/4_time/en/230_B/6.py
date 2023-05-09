def main():
    S = input()
    T = "o" + S + "x"
    print("Yes" if T in "oxx" * 100000 else "No")
