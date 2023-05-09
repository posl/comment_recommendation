def main():
    #input
    n = int(input())
    xys = [tuple(map(int, input().split())) for _ in range(n)]
    #compute
    ans = 'No'
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (xys[i][0]-xys[j][0])*(xys[i][1]-xys[k][1]) == (xys[i][0]-xys[k][0])*(xys[i][1]-xys[j][1]):
                    ans = 'Yes'
                    break
    #output
    print(ans)

if __name__ == '__main__':
    main()