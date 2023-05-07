def main():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort(key=lambda x: [x.index(i) for i in x if i in x])
    print('
'.join(s))

if __name__ == '__main__':
    main()