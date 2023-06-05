def getCityInfo(N, M, citys):
    cityInfo = [0] * N
    for i in range(M):
        cityInfo[citys[i][0] - 1] += 1
        cityInfo[citys[i][1] - 1] += 1
    return cityInfo

if __name__ == '__main__':
    getCityInfo()