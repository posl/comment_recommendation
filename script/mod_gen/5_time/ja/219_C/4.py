def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda x: "".join([chr(97 + x.index(i)) for i in x]))
    print("\n".join(s))

if __name__ == '__main__':
    main()