def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(max(set(s), key=s.count))

if __name__ == '__main__':
    main()