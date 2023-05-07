def main():
    s = input()
    s_inv = s[::-1]
    if s == s_inv:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()