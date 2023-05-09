def calc(N,K):
    ans = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            ans += int(str(i) + '0' + str(j))
    return ans

if __name__ == '__main__':
    calc()