def main():
    S = input()
    T = input()
    if T.startswith(S) and len(T) == len(S) + 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()