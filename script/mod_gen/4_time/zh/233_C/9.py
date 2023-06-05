def main():
    n,x = map(int,input().split())
    bag = []
    for i in range(n):
        bag.append(list(map(int,input().split())))
    print(bag)
    res = 0
    for i in range(n):
        for j in range(len(bag[i])):
            if bag[i][j] == x:
                res += 1
            for k in range(i+1,n):
                if bag[i][j]*bag[k][j] == x:
                    res += 1
    print(res)

if __name__ == '__main__':
    main()