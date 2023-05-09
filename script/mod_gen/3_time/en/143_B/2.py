def main():
    N = int(input())
    d = list(map(int,input().split()))
    res = 0
    for i in range(N):
        for j in range(i+1,N):
            res += d[i] * d[j]
    print(res)

if __name__ == '__main__':
    main()