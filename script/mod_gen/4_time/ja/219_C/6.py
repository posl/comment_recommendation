def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x.translate(str.maketrans(x, x, x)) for x in 'zyxwvutsrqponmlkjihgfedcba'.translate(str.maketrans('zyxwvutsrqponmlkjihgfedcba', 'abcdefghijklmnopqrstuvwxyz'))])
    print("\n".join(s))

if __name__ == '__main__':
    main()