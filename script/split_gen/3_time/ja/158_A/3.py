def main():
    S = input()
    if S.count("A") == 1 and S.count("B") == 2:
        print("Yes")
    elif S.count("A") == 2 and S.count("B") == 1:
        print("Yes")
    else:
        print("No")
