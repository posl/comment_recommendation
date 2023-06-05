def main():
    n,k = map(int,input().split())
    l = []
    for i in range(n):
        a,b = map(int,input().split())
        l.append([a,b])
    l.sort()
    for i in range(n):
        if k < l[i][0]:
            break
        else:
            k += l[i][1]
    print(k)

if __name__ == '__main__':
    main()