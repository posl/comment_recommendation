def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    print len(set(a))

if __name__ == '__main__':
    main()