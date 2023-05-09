def main():
    s = input()
    s_set = set(s)
    for i in s_set:
        if s.count(i) == 1:
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()