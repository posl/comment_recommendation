def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(i+1,n):
            if names[i][0]==names[j][0] and names[i][1]==names[j][1]:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()