def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,M,A)
    #累计和
    cumsum = [0]
    for i in range(0,N):
        cumsum.append(cumsum[i]+A[i])
    #print(cumsum)
    #最大值
    maxsum = -10000000000
    for i in range(0,N-M+1):
        #print(cumsum[i+M]-cumsum[i])
        if cumsum[i+M]-cumsum[i] > maxsum:
            maxsum = cumsum[i+M]-cumsum[i]
    print(maxsum)
