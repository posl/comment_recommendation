def main():
    s = input()
    sum = 0
    for i in range(4):
        if s[i] == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)

if __name__ == '__main__':
    main()