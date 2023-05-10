def main():
    X = input()
    if X == X[0]*4:
        print("Weak")
        return
    for i in range(3):
        if int(X[i]) == 9:
            if int(X[i+1]) != 0:
                print("Strong")
                return
        else:
            if int(X[i+1]) != int(X[i])+1:
                print("Strong")
                return
    print("Weak")
