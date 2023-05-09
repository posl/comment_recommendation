def main():
    # N = int(input())
    # shops = []
    # for _ in range(N):
    #     a, p, x = map(int, input().split())
    #     shops.append([a, p, x])
    # print(shops)
    # result = -1
    # for shop in shops:
    #     if shop[2] > 0:
    #         if result == -1:
    #             result = shop[1]
    #         elif shop[1] < result:
    #             result = shop[1]
    #         else:
    #             pass
    # print(result)
    N = int(input())
    A = []
    P = []
    X = []
    for _ in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    result = -1
    for i in range(N):
        if X[i] > 0:
            if result == -1:
                result = P[i]
            elif P[i] < result:
                result = P[i]
            else:
                pass
    print(result)

if __name__ == '__main__':
    main()