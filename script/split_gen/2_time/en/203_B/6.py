def main():
    #write code here
    N,K = map(int,input().split())
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum += int(str(i) + '0' + str(j))
    print(sum)
