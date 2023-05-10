def main():
    n,m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(8):
        xyz.sort(reverse=True, key=lambda x: (x[0]*(-1)**(i&1), x[1]*(-1)**((i>>1)&1), x[2]*(-1)**((i>>2)&1)))
        tmp = [0,0,0]
        for j in range(m):
            tmp[0] += xyz[j][0]
            tmp[1] += xyz[j][1]
            tmp[2] += xyz[j][2]
        ans = max(ans, abs(tmp[0]) + abs(tmp[1]) + abs(tmp[2]))
    print(ans)

if __name__ == '__main__':
    main()