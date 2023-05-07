def main():
    #N, D = map(int, input().split())
    #X = []
    #Y = []
    #for i in range(N):
    #    x, y = map(int, input().split())
    #    X.append(x)
    #    Y.append(y)
    N, D = 20, 100000
    X = [14309, -56855, 151364, 103789, 147404, -37006, 188810, 13419, -88280, -196399, -176527, 46659, -153551, 98784, 94111, -30401, -55056, 5901, 138819, -69848]
    Y = [-32939, 100340, 25430, -113141, -136977, -30929, -49557, 70401, 165170, 137941, -61904, 115261, 114185, -6820, -86268, 61477, 7872, -163796, -185986, -96669]
    cnt = 0
    for i in range(N):
        if X[i]**2 + Y[i]**2 <= D**2:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()