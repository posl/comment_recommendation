def main():
    s = int(input())
    a = [s]
    while True:
        if a[-1] % 2 == 0:
            a.append(int(a[-1] / 2))
        else:
            a.append(3 * a[-1] + 1)
        if a.count(a[-1]) == 2:
            break
    print(len(a))

if __name__ == '__main__':
    main()