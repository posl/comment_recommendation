def main():
    s = input()
    count = 0
    for i in s:
        if i == '+':
            count += 1
        else:
            count -= 1
    print(count)

if __name__ == '__main__':
    main()