def main():
    N, M = map(int, input().split())
    data = []
    for i in range(M):
        data.append(list(map(int, input().split())))
    #print(N, M, data)
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            #print(i, j, data[i], data[j])
            if data[i][0] in data[j] and data[i][1] in data[j]:
                ans += 1
            if data[i][0] in data[j] and data[i][1] in data[j]:
                ans += 1
            if data[i][0] in data[j] and data[i][1] in data[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()