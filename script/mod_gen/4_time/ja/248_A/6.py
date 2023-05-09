def main():
    s = input()
    s = list(map(int, s))
    s.sort()
    for i in range(10):
        if i in s:
            continue
        else:
            print(i)
            return

if __name__ == '__main__':
    main()