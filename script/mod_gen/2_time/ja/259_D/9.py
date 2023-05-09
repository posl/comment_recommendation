def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    ret = "No"
    for i in range(N):
        if (circles[i][0] - sx)**2 + (circles[i][1] - sy)**2 < circles[i][2]**2 and (circles[i][0] - tx)**2 + (circles[i][1] - ty)**2 < circles[i][2]**2:
            ret = "Yes"
            break
    print(ret)

if __name__ == '__main__':
    main()