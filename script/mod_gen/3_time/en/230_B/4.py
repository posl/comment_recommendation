def main():
    S = input()
    T = "oxx" * (10 ** 5)
    if S in T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()