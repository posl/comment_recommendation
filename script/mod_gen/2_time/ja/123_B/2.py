def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = [a, b, c, d, e]
    time.sort()
    if time[4] % 10 == 0:
        print(time[4] * 4)
    else:
        print(time[4] // 10 * 10 * 4 + 10 * 4)

if __name__ == '__main__':
    main()