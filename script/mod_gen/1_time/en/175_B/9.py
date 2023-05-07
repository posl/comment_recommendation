def main():
    #N = int(input())
    #L = list(map(int, input().split()))
    N = 10
    L = [9, 4, 6, 1, 9, 6, 10, 6, 6, 8]
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()