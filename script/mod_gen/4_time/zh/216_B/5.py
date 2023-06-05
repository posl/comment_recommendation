def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        names.append(name)
    print(names)
    for i in range(n):
        for j in range(i+1,n):
            if names[i][0]==names[j][0] and names[i][1]==names[j][1]:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()