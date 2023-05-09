def main():
    n = int(input())
    ab = []
    for i in range(n):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(n):
        if i % 2 == 0:
            takahashi += ab[i][0]
        else:
            aoki += ab[i][1]
    if takahashi > aoki:
        print(0)
        return
    else:
        for i in range(n):
            if i % 2 == 0:
                takahashi += ab[i][1] - ab[i][0]
            else:
                aoki += ab[i][0] - ab[i][1]
            if takahashi > aoki:
                print(i+1)
                return

if __name__ == '__main__':
    main()