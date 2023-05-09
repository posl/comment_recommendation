def main():
    n = int(input())
    s = [input().split() for i in range(n)]
    t = sorted(s, key=lambda x: int(x[1]), reverse=True)
    print(t[1][0])

if __name__ == '__main__':
    main()