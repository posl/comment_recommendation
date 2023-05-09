def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print('Weak')
    elif int(X[0]) == (int(X[1]) + 1) % 10 and int(X[1]) == (int(X[2]) + 1) % 10 and int(X[2]) == (int(X[3]) + 1) % 10:
        print('Weak')
    else:
        print('Strong')
