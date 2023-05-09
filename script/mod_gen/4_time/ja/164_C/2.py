def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))

if __name__ == '__main__':
    main()