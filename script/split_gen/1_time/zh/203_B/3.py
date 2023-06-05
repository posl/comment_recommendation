def main():
    N,K = map(int,input().split())
    sum = 0
    for i in range(1,N+1):
        for j in range(1,K+1):
            sum += 100*i+j
    print(sum)
main()
