def main():
    N = int(input())
    a = [0 for _ in range(N-1)]
    b = [0 for _ in range(N-1)]
    for i in range(N-1):
        a[i], b[i] = map(int, input().split())
    if N == 3:
        print('Yes')
        return
    if N == 4:
        if a[0] == a[1] or a[0] == b[1] or b[0] == a[1] or b[0] == b[1]:
            print('Yes')
            return
        else:
            print('No')
            return
    else:
        if a[0] == a[1] or a[0] == b[1] or b[0] == a[1] or b[0] == b[1]:
            for i in range(2, N-1):
                if a[0] != a[i] and a[0] != b[i] and b[0] != a[i] and b[0] != b[i]:
                    print('No')
                    return
            print('Yes')
            return
        else:
            print('No')
            return

if __name__ == '__main__':
    main()