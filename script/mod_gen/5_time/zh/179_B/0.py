def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int, input().split())))
    for i in range(N-2):
        if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()