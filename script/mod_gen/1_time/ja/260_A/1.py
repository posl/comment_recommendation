def main():
    s = input()
    for i in s:
        if s.count(i) == 1:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()