def main():
    x = input()
    n = int(input())
    s = [input() for i in range(n)]
    x = x.lower()
    s.sort(key=lambda x: [x.translate(str.maketrans(x, x.lower())), x])
    for i in s:
        print(i)

if __name__ == '__main__':
    main()