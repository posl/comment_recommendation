def main():
    s = input()
    sum = 0
    for c in s:
        if c == '+':
            sum += 1
        else:
            sum -= 1
    print(sum)

if __name__ == '__main__':
    main()