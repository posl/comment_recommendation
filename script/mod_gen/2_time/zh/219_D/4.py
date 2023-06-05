def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: [x.index(c) for c in x])
    s.sort(key=lambda x: [x.index(c) for c in x], reverse=True)
    print(s)
    print(x)
    print(n)
    print(s)

if __name__ == '__main__':
    main()