def main():
    N, M = map(int, input().split())
    cond = [tuple(map(int, input().split())) for _ in range(M)]
    K = int(input())
    dish = [tuple(map(int, input().split())) for _ in range(K)]
    ans = 0
    for i in range(2**K):
        dish_on = [False] * N
        for j in range(K):
            if (i >> j) & 1:
                dish_on[dish[j][1]-1] = True
            else:
                dish_on[dish[j][0]-1] = True
        cnt = 0
        for c in cond:
            if dish_on[c[0]-1] and dish_on[c[1]-1]:
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(ans)

if __name__ == '__main__':
    main()