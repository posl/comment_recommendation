def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(str, input().split())))
    m.sort(key=lambda x: int(x[1]), reverse=True)
    print(m[1][0])

if __name__ == '__main__':
    main()