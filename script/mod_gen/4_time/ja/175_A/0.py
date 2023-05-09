def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i == 'R':
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

if __name__ == '__main__':
    main()