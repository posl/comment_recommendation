def main():
    # N = int(input())
    # L = list(map(int, input().split()))
    N = 7
    L = [218, 786, 704, 233, 645, 728, 389]
    # N = 4
    # L = [3, 4, 2, 1]
    # N = 3
    # L = [1, 1000, 1]
    ans = 0
    L.sort()
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] + L[j] > L[k]:
                    ans += 1
                else:
                    break
    print(ans)

if __name__ == '__main__':
    main()