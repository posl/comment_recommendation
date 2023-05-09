def main():
    S = input()
    T = "o" + "x" + "x" * len(S) + "o" * len(S)
    print("Yes" if S in T else "No")

if __name__ == '__main__':
    main()