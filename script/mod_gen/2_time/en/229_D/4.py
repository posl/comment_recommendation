def main():
    S = input()
    K = int(input())
    S = S.replace("..", ".")
    if K == 0:
        print(S.count("X"))
    else:
        S = S.replace(".", "X", K)
        print(S.count("X"))
main()

if __name__ == '__main__':
    main()