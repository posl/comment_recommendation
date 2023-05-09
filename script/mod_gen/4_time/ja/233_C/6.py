def main():
    n,x = map(int, input().split())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        for j in range(l[i][0]):
            if x % l[i][j+1] == 0:
                #print("i,j", i,j)
                count += 1
    print(count)

if __name__ == '__main__':
    main()