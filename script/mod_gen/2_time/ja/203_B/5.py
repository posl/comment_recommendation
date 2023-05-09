def main():
    N, K = map(int, input().split())
    result = 0
    for i in range(N):
        for j in range(K):
            result += (i+1)*100 + (j+1)
    print(result)

if __name__ == '__main__':
    main()