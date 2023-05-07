def main():
    s = input()
    for i in s:
        if s.count(i) == 1:
            print(i)
            exit()
    print(-1)
    exit()

if __name__ == '__main__':
    main()