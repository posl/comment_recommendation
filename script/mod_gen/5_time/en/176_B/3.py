def main():
    n = input()
    if sum([int(i) for i in n]) % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()