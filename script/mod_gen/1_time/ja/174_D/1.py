def main():
    N = int(input())
    S = input()
    R = S.count("R")
    W = S.count("W")
    print(min(R, W))

if __name__ == '__main__':
    main()