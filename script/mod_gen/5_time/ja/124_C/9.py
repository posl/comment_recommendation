def main():
    s = input()
    n = len(s)
    ans = min(s.count("0"), s.count("1"))
    print(ans * 2)

if __name__ == '__main__':
    main()