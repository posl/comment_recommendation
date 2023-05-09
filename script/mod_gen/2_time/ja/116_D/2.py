def main():
    N, K = map(int, input().split())
    sushi = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    #print(sushi)
    satsufy = 0
    kind = 0
    kind_list = []
    for i in range(K):
        satsufy += sushi[i][1]
        if sushi[i][0] not in kind_list:
            kind += 1
            kind_list.append(sushi[i][0])
    satsufy += kind * kind
    #print(satsufy)
    #print(kind)
    #print(kind_list)
    for i in range(K, N):
        if sushi[i][0] in kind_list:
            continue
        if sushi[i][1] < sushi[K-1][1]:
            break
        satsufy -= sushi[K-1][1]
        satsufy += sushi[i][1]
        satsufy -= kind * kind
        kind += 1
        kind_list.append(sushi[i][0])
        satsufy += kind * kind
        #print(satsufy)
        #print(kind)
        #print(kind_list)
    print(satsufy)

if __name__ == '__main__':
    main()