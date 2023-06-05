def main():
    N = int(input())
    d = []
    for i in range(N):
        d.append(list(map(int, input().split())))
    for i in range(N-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()