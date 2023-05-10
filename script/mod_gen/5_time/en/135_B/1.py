def main():
    n = int(input())
    p = list(map(int, input().split()))
    p_sorted = sorted(p)
    count = 0
    for i in range(n):
        if p[i] != p_sorted[i]:
            count += 1
    if count <= 2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()