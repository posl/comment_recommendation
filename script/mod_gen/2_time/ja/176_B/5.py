def main():
    n = input()
    print("Yes" if sum([int(i) for i in n]) % 9 == 0 else "No")

if __name__ == '__main__':
    main()