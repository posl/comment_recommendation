def main():
    S = input()
    S = S.replace("o", "")
    if len(S) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()