def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #print("---------")
    for k in range(1, N):
        #print(k)
        #print("---------")
        count = 0
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                #print(i, j)
                if (abs(i-j) == k) or (abs(i-X) + abs(j-Y) + 1 == k) or (abs(i-Y) + abs(j-X) + 1 == k):
                    count += 1
                    #print("count up")
        print(count)

if __name__ == '__main__':
    main()