def main():
    S = input()
    count = 0
    for i in S:
        if i == "+":
            count += 1
        elif i == "-":
            count -= 1
    print(count)

if __name__ == '__main__':
    main()