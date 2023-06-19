def main():
    p = list(map(int, input().split()))
    s = []
    for i in p:
        s.append(chr(ord('a') + i - 1))
    print(''.join(s))

if __name__ == '__main__':
    main()