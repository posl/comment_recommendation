def main():
    n, m, q = map(int, input().split())
    abcd = []
    for i in range(q):
        abcd.append(list(map(int, input().split())))
    print(abcd)

if __name__ == '__main__':
    main()