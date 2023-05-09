def main():
    N = int(input())
    #print(N)
    result = 0
    a = []
    for i in range(N):
        a.append(list(map(int,input().split())))
    #print(a)
    for i in range(N-1):
        if a[i][0] == a[i+1][0]:
            for j in range(1,len(a[i])):
                if a[i][j] != a[i+1][j]:
                    result += 1
                    break
        else:
            result += 1
    print(N-result)

if __name__ == '__main__':
    main()