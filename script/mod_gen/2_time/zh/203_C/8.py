def main():
    N, K = map(int, input().split())
    villagelist = []
    for i in range(N):
        A, B = map(int, input().split())
        villagelist.append([A, B])
    villagelist.sort()
    sum = 0
    for i in range(N):
        if villagelist[i][0] - sum <= K:
            K -= villagelist[i][0] - sum
            sum = villagelist[i][0]
            K += villagelist[i][1]
        else:
            print(sum + K)
            exit()
    print(sum + K)

if __name__ == '__main__':
    main()