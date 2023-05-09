def main():
    N = int(input())
    Nlist = []
    for i in range(N):
        Nlist.append(input().split())
    for i in range(N):
        for j in range(i+1,N):
            if Nlist[i][0] == Nlist[j][0] and Nlist[i][1] == Nlist[j][1]:
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()