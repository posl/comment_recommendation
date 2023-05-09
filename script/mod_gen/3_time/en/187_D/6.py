def main():
    N = int(input())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        if takahashi < aoki:
            takahashi += AB[i][0]
            aoki += AB[i][1]
        else:
            takahashi += AB[i][1]
            aoki += AB[i][0]
    if takahashi < aoki:
        print(N)
    else:
        print(N-1)

if __name__ == '__main__':
    main()