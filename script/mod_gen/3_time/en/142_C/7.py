def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        print(a.index(i + 1) + 1)

if __name__ == '__main__':
    main()