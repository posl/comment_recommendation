def main():
    N = int(input())
    d = []
    for i in range(N):
        d.append(input().split())
    flag = 0
    for i in range(N-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            flag = 1
    if flag == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()