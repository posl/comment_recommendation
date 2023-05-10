def main():
    n = input()
    sum = 0
    for c in n:
        sum += int(c)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()