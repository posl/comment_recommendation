def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input().split())
    nicknames = []
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    nicknames.append(names[i][0])
                    nicknames.append(names[i][1])
                    break
    if len(nicknames) == n:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()