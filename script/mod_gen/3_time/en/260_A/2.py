def main():
    s = input()
    for c in s:
        if s.count(c) == 1:
            print(c)
            return
    print(-1)
main()

if __name__ == '__main__':
    main()