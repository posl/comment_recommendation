def main():
    N = int(input())
    S = input()
    R = S.count("R")
    W = S.count("W")
    if R == 0 or W == 0:
        print(0)
    else:
        print(min(R,W))

if __name__ == '__main__':
    main()