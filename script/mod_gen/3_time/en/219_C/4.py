def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s = sorted(s, key=lambda x: [x.index(c) for c in x])
    for i in s:
        print(i)

if __name__ == '__main__':
    main()