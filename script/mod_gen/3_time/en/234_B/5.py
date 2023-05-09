def main():
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans, (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
    print(ans**0.5)
main()

if __name__ == '__main__':
    main()