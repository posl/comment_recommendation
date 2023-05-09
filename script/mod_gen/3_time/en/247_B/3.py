def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if names[i][0] == names[j][0] or names[i][0] == names[j][1] or names[i][1] == names[j][0] or names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()