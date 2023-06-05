def main():
    n = int(input())
    a = list(map(int, input().split()))
    n = 2 ** n
    index = [i for i in range(n)]
    while len(index) > 2:
        tmp = []
        for i in range(0, len(index), 2):
            if a[index[i]] > a[index[i + 1]]:
                tmp.append(index[i])
            else:
                tmp.append(index[i + 1])
        index = tmp
    if a[index[0]] < a[index[1]]:
        print(index[0] + 1)
    else:
        print(index[1] + 1)

if __name__ == '__main__':
    main()