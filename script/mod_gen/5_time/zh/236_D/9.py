def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(a)

if __name__ == '__main__':
    main()