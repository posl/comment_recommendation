def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()