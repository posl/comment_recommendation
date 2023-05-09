def main():
    s = input()
    s = list(map(int, s))
    for i in range(10):
        if i not in s:
            print(i)
            return

if __name__ == '__main__':
    main()