def main():
    n,d = map(int,input().split())
    walls = []
    for i in range(n):
        walls.append(list(map(int,input().split())))
    walls.sort(key=lambda x:x[0])
    #print(walls)
    #print(n,d)
    #print(walls)
    i = 0
    j = 0
    count = 0
    while i < n:
        if j < n and walls[j][0] - walls[i][0] < d:
            count += 1
            j += 1
        else:
            count -= 1
            i += 1
    print(count)

if __name__ == '__main__':
    main()