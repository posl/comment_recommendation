def main():
    N, M = list(map(int, input().split()))
    xyz = []
    for i in range(N):
        x, y, z = list(map(int, input().split()))
        xyz.append([x, y, z])
    ans = 0
    for i in range(2 ** 3):
        op = [1, 1, 1]
        for j in range(3):
            if i & (2 ** j) != 0:
                op[j] = -1
        xyz.sort(key=lambda x: op[0] * x[0] + op[1] * x[1] + op[2] * x[2], reverse=True)
        t = 0
        for j in range(M):
            t += op[0] * xyz[j][0] + op[1] * xyz[j][1] + op[2] * xyz[j][2]
        ans = max(ans, abs(t))
    print(ans)

if __name__ == '__main__':
    main()