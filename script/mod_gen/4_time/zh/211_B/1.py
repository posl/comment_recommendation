def main():
    s = set()
    for _ in range(4):
        s.add(input())
    if len(s) == 4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()