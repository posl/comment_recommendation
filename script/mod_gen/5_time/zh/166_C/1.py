def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    H.insert(0, 0)
    #print(H)
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print(AB)
    result = [1] * (N+1)
    for i in range(M):
        if H[AB[i][0]] < H[AB[i][1]]:
            result[AB[i][0]] = 0
        elif H[AB[i][0]] > H[AB[i][1]]:
            result[AB[i][1]] = 0
        elif H[AB[i][0]] == H[AB[i][1]]:
            result[AB[i][0]] = 0
            result[AB[i][1]] = 0
    print(sum(result))

if __name__ == '__main__':
    main()