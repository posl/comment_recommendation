def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
    elif X[0] == X[1] and X[1] == X[2] and X[2] == str(int(X[3]) - 1):
        print("Weak")
    elif X[0] == X[1] and X[1] == str(int(X[2]) - 1) and X[2] == str(int(X[3]) - 1):
        print("Weak")
    elif X[0] == str(int(X[1]) - 1) and X[1] == str(int(X[2]) - 1) and X[2] == str(int(X[3]) - 1):
        print("Weak")
    else:
        print("Strong")
