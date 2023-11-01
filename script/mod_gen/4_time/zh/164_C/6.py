def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(len(set(s)))

if __name__ == '__main__':
    main()