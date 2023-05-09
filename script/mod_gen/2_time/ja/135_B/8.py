def main():
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        if p[i] == i+1:
            continue
        if i+1 in p:
            j = p.index(i+1)
            p[i], p[j] = p[j], p[i]
        else:
            print('NO')
            return
    print('YES')

if __name__ == '__main__':
    main()