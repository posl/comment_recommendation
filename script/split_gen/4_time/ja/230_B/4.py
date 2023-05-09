def main():
    S = input()
    if S.count("o") == 0:
        print("No")
        return
    if S.count("x") == 0:
        print("Yes")
        return
    print("Yes")
