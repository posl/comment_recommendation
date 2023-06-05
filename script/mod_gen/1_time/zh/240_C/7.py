def main():
    n, x = map(int, input().split())
    a_b = []
    for _ in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[1])
    for i in range(n):
        if x < a_b[i][0]:
            print('No')
            return
        x += a_b[i][1] - a_b[i][0]
    print('Yes')

if __name__ == '__main__':
    main()