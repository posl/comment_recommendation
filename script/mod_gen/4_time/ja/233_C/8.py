def main():
    n,x = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    #print(l)
    count = 0
    for i in range(n):
        for j in range(l[i][0]):
            if x % l[i][j+1] == 0:
                count += 1
    print(count)
main()

if __name__ == '__main__':
    main()