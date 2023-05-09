def main():
    n = int(input())
    s = input().split()
    for i in range(n):
        print(s[0][i] + s[1][i], end='')

if __name__ == '__main__':
    main()