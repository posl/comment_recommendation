def main():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input().split())
    for i in range(n):
        if i == 0:
            if name[0][0] == name[1][0] or name[0][0] == name[1][1] or name[0][1] == name[1][0] or name[0][1] == name[1][1]:
                print('Yes')
                break
            else:
                print('No')
                break
        elif i == n-1:
            if name[i][0] == name[i-1][0] or name[i][0] == name[i-1][1] or name[i][1] == name[i-1][0] or name[i][1] == name[i-1][1]:
                print('Yes')
                break
            else:
                print('No')
                break
        else:
            if name[i][0] == name[i-1][0] or name[i][0] == name[i-1][1] or name[i][1] == name[i-1][0] or name[i][1] == name[i-1][1]:
                if name[i][0] == name[i+1][0] or name[i][0] == name[i+1][1] or name[i][1] == name[i+1][0] or name[i][1] == name[i+1][1]:
                    print('Yes')
                    break
                else:
                    print('No')
                    break
            else:
                print('No')
                break

if __name__ == '__main__':
    main()