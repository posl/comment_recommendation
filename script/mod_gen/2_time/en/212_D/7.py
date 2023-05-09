def main():
    #input
    Q = int(input())
    PQX = [list(map(int, input().split())) for _ in range(Q)]
    #solve
    ans = [0] * Q
    que = []
    add = 0
    for i, (p, x) in enumerate(PQX):
        if p == 1:
            que.append(x-add)
        elif p == 2:
            add += x
        else:
            ans[i] = min(que) + add
            que.remove(min(que))
    #output
    for i in range(Q):
        if PQX[i][0] == 3:
            print(ans[i])

if __name__ == '__main__':
    main()