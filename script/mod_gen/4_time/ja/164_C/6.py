def main():
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    print(len(s))

if __name__ == '__main__':
    main()