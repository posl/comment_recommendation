def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    if L[i] + L[j] > L[k]:
                        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()