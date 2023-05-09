def main():
    N = int(input())
    L = list(map(int, input().split()))
    #L.sort(reverse=True)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                    continue
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()