def main():
    n = int(input())
    s = [1]
    for i in range(1, n):
        s = s + [i + 1] + s
    print(*s, sep=' ')

if __name__ == '__main__':
    main()