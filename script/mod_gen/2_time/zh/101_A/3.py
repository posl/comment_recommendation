def main():
    S = input()
    num = 0
    for i in range(4):
        if S[i] == '+':
            num += 1
        else:
            num -= 1
    print(num)

if __name__ == '__main__':
    main()