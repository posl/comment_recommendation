def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input().split())
    name = sorted(name, key=lambda x: (x[0], x[1]))
    for i in range(N-1):
        if name[i][0] == name[i+1][0] and name[i][1] == name[i+1][1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()