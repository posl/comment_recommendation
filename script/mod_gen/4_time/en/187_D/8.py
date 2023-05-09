def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[0]+x[1], reverse=True)
    aoki = 0
    takahashi = 0
    for i in range(N):
        if i % 2 == 0:
            aoki += AB[i][0]
        else:
            takahashi += AB[i][1]
    print(aoki - takahashi)
main()

if __name__ == '__main__':
    main()