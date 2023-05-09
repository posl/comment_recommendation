def main():
    # input
    X = input()
    # compute
    is_weak = True
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        is_weak = True
    else:
        is_weak = False
    if (int(X[1])+1)%10 == int(X[2]) and (int(X[2])+1)%10 == int(X[3]):
        is_weak = True
    else:
        is_weak = False
    # output
    if is_weak:
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()