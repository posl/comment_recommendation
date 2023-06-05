def main():
    x = input()
    n = int(input())
    s = [input() for i in range(n)]
    d = {c: i for i, c in enumerate(x)}
    s.sort(key=lambda x: [d[c] for c in x])
    print(*s, sep='\n')

if __name__ == '__main__':
    main()