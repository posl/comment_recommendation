def main():
    s = input()
    s = list(s)
    s = list(map(int, s))
    s.sort()
    for i in range(1, 10):
        if i not in s:
            print(i)
            break

if __name__ == '__main__':
    main()