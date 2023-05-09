def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = []
    for i in range(N):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    ans = "No"
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            if (x1-x2)**2 + (y1-y2)**2 < (r1+r2)**2:
                ans = "Yes"
                break
        if ans == "Yes":
            break
    print(ans)

if __name__ == '__main__':
    main()