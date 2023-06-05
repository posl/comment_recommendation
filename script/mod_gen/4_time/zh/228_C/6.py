def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for i in range(n)]
    print(p)
    for i in range(n):
        p[i].append(sum(p[i]))
    print(p)
    p.sort(key=lambda x: x[3], reverse=True)
    print(p)
    for i in range(n):
        if p[i][3] > p[k-1][3]:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()