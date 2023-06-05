def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i]+L[j] > L[k]:
                    cnt += 1
    print(cnt)
main()
