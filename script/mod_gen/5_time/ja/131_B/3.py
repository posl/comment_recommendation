def main():
    N, L = map(int, input().split())
    ans = 0
    minv = 10000
    for i in range(0, N):
        tmp = L + i
        if(abs(tmp) < minv):
            minv = abs(tmp)
            ans = tmp
    print((N-1)*N//2 + ans)

if __name__ == '__main__':
    main()