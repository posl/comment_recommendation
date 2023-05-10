def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()