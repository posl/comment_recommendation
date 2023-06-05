def main():
    n,m = map(int,input().split())
    k = [0]*n
    a = [0]*n
    for i in range(n):
        k[i],*a[i] = map(int,input().split())
    count = 0
    for i in range(1,m+1):
        flag = True
        for j in range(n):
            if i in a[j]:
                pass
            else:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()