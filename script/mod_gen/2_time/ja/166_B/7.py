def main():
    N, K = map(int, input().split())
    #print(N, K)
    count = 0
    for i in range(K):
        d = int(input())
        #print(d)
        for j in range(d):
            A = int(input())
            #print(A)
            if A == 1:
                count += 1
                break
    print(N - count)

if __name__ == '__main__':
    main()