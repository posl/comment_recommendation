def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l = [tuple(x) for x in l]
    print(len(set(l)))

if __name__ == '__main__':
    main()