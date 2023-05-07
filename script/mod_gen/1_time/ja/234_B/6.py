def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            ans = max(ans,(p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)
    print(ans**0.5)

if __name__ == '__main__':
    main()