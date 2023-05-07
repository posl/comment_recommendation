def main():
    x = input()
    if x[0].isupper() and x[7].isupper() and len(x) == 8 and x[1:7].isdigit() and 100000 <= int(x[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()