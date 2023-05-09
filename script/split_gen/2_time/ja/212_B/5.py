def main():
    X = input()
    if X[0] == X[1] == X[2] == X[3]:
        print('Weak')
    else:
        if (int(X[0])+1)%10 == int(X[1]) and (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
            print('Weak')
        else:
            print('Strong')
