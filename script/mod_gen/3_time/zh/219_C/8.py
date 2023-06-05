def main():
    x = input()
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s.sort(key=lambda x: [x.translate(str.maketrans(x, 'abcdefghijklmnopqrstuvwxyz'))])
    print('\n'.join(s))

if __name__ == '__main__':
    main()