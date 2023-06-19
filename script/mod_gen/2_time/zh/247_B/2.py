def main():
    n = int(input())
    names = [input().split() for _ in range(n)]
    for i in range(n):
        names[i].append(i)
    names.sort(key=lambda x: x[0])
    for i in range(n):
        names[i].append(i)
    names.sort(key=lambda x: x[1])
    for i in range(1, n):
        if names[i-1][0] == names[i][0] and names[i-1][1] == names[i][1]:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()