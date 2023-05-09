def main():
    n = int(input())
    p = list(map(int, input().split()))
    sorted_p = sorted(p)
    if p == sorted_p:
        print('YES')
        exit()
    for i in range(n):
        for j in range(i+1, n):
            p[i], p[j] = p[j], p[i]
            if p == sorted_p:
                print('YES')
                exit()
            p[i], p[j] = p[j], p[i]
    print('NO')

if __name__ == '__main__':
    main()