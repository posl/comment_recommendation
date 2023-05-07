def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()