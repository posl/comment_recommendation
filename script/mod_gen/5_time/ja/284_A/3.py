def main():
    n = int(input())
    s = [input() for i in range(n)]
    s.reverse()
    print("\n".join(s))

if __name__ == '__main__':
    main()