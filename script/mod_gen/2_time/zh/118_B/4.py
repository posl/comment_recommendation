def main():
    n,m = map(int,input().split())
    k = []
    for i in range(n):
        k.append(list(map(int,input().split())))
    result = 0
    for i in range(1,m+1):
        flag = True
        for j in range(n):
            if i not in k[j][1:]:
                flag = False
                break
        if flag:
            result += 1
    print(result)

if __name__ == '__main__':
    main()