def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j and names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()