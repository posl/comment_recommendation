def main():
    X = input()
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        print("Weak")
        return
    for i in range(3):
        if (int(X[i]) + 1) % 10 != int(X[i+1]):
            print("Strong")
            return
    print("Weak")

if __name__ == '__main__':
    main()