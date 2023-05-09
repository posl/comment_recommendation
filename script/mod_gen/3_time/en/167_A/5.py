def main():
    S = input()
    T = input()
    print("Yes" if S == T[:-1] else "No")

if __name__ == '__main__':
    main()