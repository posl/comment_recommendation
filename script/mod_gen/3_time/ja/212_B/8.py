def main():
    X = input()
    X = list(map(int, X))
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
        return
    if X[0] == 9 and X[1] == 0:
        if X[2] == 1 and X[3] == 2:
            print("Weak")
            return
    if X[0]+1 == X[1] and X[1]+1 == X[2] and X[2]+1 == X[3]:
        print("Weak")
        return
    print("Strong")
    return

if __name__ == '__main__':
    main()