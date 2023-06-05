def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    a = sorted(a)
    print a[-2]

if __name__ == '__main__':
    main()