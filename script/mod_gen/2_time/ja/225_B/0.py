def main():
    n = int(input())
    a = [0] * (n - 1)
    b = [0] * (n - 1)
    for i in range(n - 1):
        a[i], b[i] = map(int, input().split())
    
    #print(a)
    #print(b)
    
    #頂点1から辿れる頂点の数を数える
    cnt = 0
    for i in range(n - 1):
        if a[i] == 1:
            cnt += 1
        elif b[i] == 1:
            cnt += 1
    
    #print(cnt)
    
    #頂点1から辿れる頂点の数が頂点数-1であればスター
    if cnt == n - 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()