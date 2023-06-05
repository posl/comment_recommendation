def main():
    N, M = map(int, input().split())
    lst = []
    for i in range(M):
        lst.append(list(map(int, input().split())))
    lst = sorted(lst, key=lambda x: x[1])
    dic = {}
    for i in range(M):
        if lst[i][0] not in dic:
            dic[lst[i][0]] = 1
        else:
            dic[lst[i][0]] += 1
        print(str(lst[i][0]).zfill(6) + str(dic[lst[i][0]]).zfill(6))

if __name__ == '__main__':
    main()