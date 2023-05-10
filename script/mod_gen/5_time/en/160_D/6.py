def main():
    n,x,y = map(int,input().split())
    n = n - 1
    x = x - 1
    y = y - 1
    result = {}
    for i in range(n):
        for j in range(i+1,n+1):
            if i <= x and j <= x:
                result[j-i] = result.get(j-i,0) + 1
            elif i <= x and j > x and j <= y:
                result[min(j-i,i+1+x-j)] = result.get(min(j-i,i+1+x-j),0) + 1
            elif i <= x and j > y:
                result[min(j-i,i+1+x-y+y-j)] = result.get(min(j-i,i+1+x-y+y-j),0) + 1
            elif i > x and i <= y and j <= y:
                result[j-i] = result.get(j-i,0) + 1
            elif i > x and i <= y and j > y:
                result[min(j-i,i+1+y-j)] = result.get(min(j-i,i+1+y-j),0) + 1
            elif i > y and j > y:
                result[j-i] = result.get(j-i,0) + 1
    for i in range(1,n):
        print(result.get(i,0))

if __name__ == '__main__':
    main()