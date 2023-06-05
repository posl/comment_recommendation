def main():
    N, M = map(int, input().split())
    data = []
    for i in range(M):
        data.append(list(map(int, input().split())))
    data.sort()
    for i in range(N):
        count = 0
        for j in range(M):
            if i+1 in data[j]:
                count += 1
        print(count, end=' ')
        for j in range(M):
            if i+1 in data[j]:
                print(data[j][0] if data[j][0] != i+1 else data[j][1], end=' ')
        print()

if __name__ == '__main__':
    main()