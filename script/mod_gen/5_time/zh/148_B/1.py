def main():
    n = int(input())
    s, t = input().split()
    for i in range(n):
        print(s[i] + t[i], end='')

if __name__ == '__main__':
    main()