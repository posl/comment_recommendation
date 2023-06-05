def main():
    n,x,y = map(int,input().split())
    uv = []
    for i in range(n-1):
        uv.append(list(map(int,input().split())))
    #print(uv)
    path = [x]
    for i in range(n-1):
        if uv[i][0] == path[-1]:
            path.append(uv[i][1])
        elif uv[i][1] == path[-1]:
            path.append(uv[i][0])
    #print(path)
    for i in range(len(path)):
        if path[i] == y:
            print(*path[:i+1])
            break

if __name__ == '__main__':
    main()